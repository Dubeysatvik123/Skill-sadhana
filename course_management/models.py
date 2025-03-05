from django.db import models
from django.conf import settings
import uuid

class CourseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, blank=True)
    sub_category = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255)
    registration_deadline = models.DateField()
    duration_weeks = models.IntegerField(choices=[(i, f'{i} weeks') for i in range(1, 9)])
    abstract = models.TextField(max_length=200)
    intro_video = models.URLField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    syllabus = models.TextField()
    objectives = models.TextField()
    outcomes = models.TextField()
    exam_scheme = models.JSONField()
    mode_of_teaching = models.JSONField()  # List of selected modes
    unique_course_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CourseApproval(models.Model):
    """ Tracks course approval status and notifies instructors """
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='approval')
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Approval Status for {self.course.name}"


class Module(models.Model):
    """ Represents a module within a course """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course.name} - {self.title}"


class VideoContent(models.Model):
    """ Represents videos within a module (for Video Mode) """
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='course_videos/', help_text="Upload MP4 video")

    def __str__(self):
        return self.title


class PDFContent(models.Model):
    """ Represents PDF uploads for a course (for PDF Mode) """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='pdfs')
    pdf_file = models.FileField(upload_to='course_pdfs/', help_text="Upload PDF File")

    def __str__(self):
        return f"PDF for {self.course.name}"


class LiveClass(models.Model):
    """ Represents a live class session (for Live Mode) """
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='live_classes')
    title = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    meet_link = models.URLField(help_text="Zoom/Meet Link")

    def __str__(self):
        return f"Live: {self.title} - {self.scheduled_time}"
