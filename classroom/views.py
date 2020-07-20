from django.shortcuts import render
from .models import Post, Notice, Module, Grade
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'modules': Module.objects.all(),
        'posts': Post.objects.all(),
        'notice': Notice.objects.all()

    }

    return render(request, 'classroom/home.html', context,
                  {'title': 'Test Page', 'homepage': 'true'})


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'classroom/grade.html'
    context_object_name = 'grades'


class ModuleListView(LoginRequiredMixin, ListView):
    model = Module
    template_name = 'classroom/module.html'
    context_object_name = 'modules'
    # module --> group

    def get_queryset(self):
        self.grade = get_object_or_404(Grade, pk=self.kwargs['pk'])
        return Module.objects.filter(grade=self.grade)

    def get_context_data(self, **kwargs):
        context = super(ModuleListView, self).get_context_data(**kwargs)
        context['grade'] = self.grade
        return context


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'classroom/home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        self.module = get_object_or_404(Module, pk=self.kwargs['pk'])
        return Post.objects.filter(module=self.module).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['module'] = self.module
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    fields = ['document']


class NoticeListView(LoginRequiredMixin, ListView):
    model = Notice
    template_name = 'classroom/notice.html'
    fields = ['notice']
    context_object_name = 'notice_obj'
    ordering = ['-date_posted']


@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView,):
    model = Post
    fields = ['title', 'content', 'module', 'grade', 'document', 'lecture',
              'reference', 'urls']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'document', 'module', 'grade']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):

    return render(request, 'classroom/about.html', {'title': 'About'})

# tested
