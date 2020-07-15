from django.test import SimpleTestCase
from django.urls import reverse, resolve
from classroom.views import GradeListView, PostListView, PostDetailView


class TestUrls(SimpleTestCase):

    def test_gradelist_urls_is_resolved(self):
        url = reverse('django-home')
        self.assertEquals(resolve(url).func.view_class, GradeListView)
        # self.assertEquals(resolve(url).func, GradeListView)
