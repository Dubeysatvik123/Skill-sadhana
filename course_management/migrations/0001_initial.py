# Generated by Django 5.1.4 on 2025-02-09 14:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sub_category', models.CharField(blank=True, max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('registration_deadline', models.DateField()),
                ('duration_weeks', models.IntegerField(choices=[(1, '1 weeks'), (2, '2 weeks'), (3, '3 weeks'), (4, '4 weeks'), (5, '5 weeks'), (6, '6 weeks'), (7, '7 weeks'), (8, '8 weeks')])),
                ('abstract', models.TextField(max_length=200)),
                ('intro_video', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('syllabus', models.TextField()),
                ('objectives', models.TextField()),
                ('outcomes', models.TextField()),
                ('exam_scheme', models.JSONField()),
                ('mode_of_teaching', models.JSONField()),
                ('unique_course_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_management.coursecategory')),
            ],
        ),
        migrations.CreateModel(
            name='CourseApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('approved_at', models.DateTimeField(auto_now=True)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='approval', to='course_management.course')),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='course_management.course')),
            ],
        ),
        migrations.CreateModel(
            name='LiveClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('scheduled_time', models.DateTimeField()),
                ('meet_link', models.URLField(help_text='Zoom/Meet Link')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_classes', to='course_management.module')),
            ],
        ),
        migrations.CreateModel(
            name='PDFContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(help_text='Upload PDF File', upload_to='course_pdfs/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='course_management.course')),
            ],
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(help_text='Upload MP4 video', upload_to='course_videos/')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='course_management.module')),
            ],
        ),
    ]
