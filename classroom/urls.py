
from django.urls import path
from . import views
from .views import (
    PostListView,
    NoticeListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ModuleListView,
    GradeListView
)

urlpatterns = [

    path('', GradeListView.as_view(), name="django-home"),
    path('module/<int:pk>', ModuleListView.as_view(), name="module"),
    path('posts/<int:pk>', PostListView.as_view(), name="post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/',
         PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',
         PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('notice/', NoticeListView.as_view(), name="notice"),
    path('about/', views.about, name="about"),

]

# git
