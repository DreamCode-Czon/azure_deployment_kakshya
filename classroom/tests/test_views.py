from django.test import TestCase, Client
from django.urls import reverse
from classroom.models import Grade
import json


class TestViews(TestCase):

    def test_gradelist_GET(self):
        client = Client()
        response = client.get(reverse('django-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'classroom/grade.html')
