from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Course, CourseCategory

class CourseTestCase(TestCase):
    def setUp(self):
        self.instructor = get_user_model().objects.create(username='testinstructor', role='instructor')
        self.category = CourseCategory.objects.create(name='Science')

    def test_create_course(self):
        course = Course.objects.create(
            instructor=self.instructor,
            name='Physics 101',
            category=self.category,
            registration_deadline='2025-12-31',
            duration_weeks=4,
            abstract='Introduction to Physics',
            intro_video='http://example.com/video.mp4',
            syllabus='Physics syllabus details...',
            objectives='Learn basic physics',
            outcomes='Understand motion and energy',
            exam_scheme={"mcqs": True},
            mode_of_teaching={"video": True}
        )
        self.assertEqual(course.name, 'Physics 101')
