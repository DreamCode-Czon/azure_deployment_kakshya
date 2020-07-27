
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Grade(models.Model):
    grade_title = models.CharField(max_length=100)
    grade_description = models.TextField(blank=True)

    def __str__(self):
        return self.grade_title


class Module(models.Model):
    module_title = models.CharField(max_length=100)
    module_description = models.TextField(blank=True)
    module_author = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.module_title


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, null=True, blank=True,
                               on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/', blank=True)
    lecture = models.FileField(upload_to='lectures/', blank=True)
    reference = models.FileField(upload_to='references/', blank=True)
    urls = models.URLField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Notice(models.Model):
    title_notice = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    notice = models.FileField(upload_to='notices', blank=True)

    def __str__(self):
        return self.title_notice

# upload_file
