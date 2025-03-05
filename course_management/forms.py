from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name', 'category', 'subject', 'registration_deadline',
            'duration_weeks', 'abstract', 'intro_video', 'thumbnail',
            'syllabus', 'objectives', 'outcomes', 'exam_scheme',
            'teaching_mode', 'video_url', 'pdf_document',
            'live_session_link', 'live_session_time'
        ]
