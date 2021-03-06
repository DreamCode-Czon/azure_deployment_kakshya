# Generated by Django 3.0.5 on 2020-05-24 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_title', models.CharField(max_length=100)),
                ('grade_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_title', models.CharField(max_length=100)),
                ('module_description', models.TextField()),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Grade')),
                ('module_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('document', models.FileField(blank=True, upload_to='documents/')),
                ('lecture', models.FileField(blank=True, upload_to='lectures/')),
                ('reference', models.FileField(blank=True, upload_to='references/')),
                ('urls', models.URLField(blank=True, max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Grade')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_notice', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('notice', models.FileField(blank=True, upload_to='notices')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
