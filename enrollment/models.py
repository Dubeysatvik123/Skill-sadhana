from django.db import models
from django.conf import settings
from course_management.models import Course
import uuid

class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)
    is_completed = models.BooleanField(default=False)
    enrolled_at = models.DateTimeField(auto_now_add=True)

class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    passing_criteria = models.IntegerField()

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()

class TestResult(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField()
    passed = models.BooleanField()
    taken_at = models.DateTimeField(auto_now_add=True)

class Certification(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='issued_certificates', on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    issued_at = models.DateTimeField(auto_now_add=True)

class Performance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    average_test_score = models.FloatField(default=0.0)
    highest_test_score = models.FloatField(default=0.0)
    lowest_test_score = models.FloatField(default=0.0)
    total_tests_taken = models.IntegerField(default=0)
    certifications_earned = models.IntegerField(default=0)
    overall_progress = models.FloatField(default=0.0)
    last_updated = models.DateTimeField(auto_now=True)

    def update_performance(self):
        test_results = TestResult.objects.filter(student=self.student, test__course=self.course)
        if test_results.exists():
            scores = [result.score for result in test_results]
            self.average_test_score = sum(scores) / len(scores)
            self.highest_test_score = max(scores)
            self.lowest_test_score = min(scores)
            self.total_tests_taken = len(scores)
        
        self.certifications_earned = Certification.objects.filter(student=self.student, course=self.course, is_approved=True).count()
        enrollment = Enrollment.objects.filter(student=self.student, course=self.course).first()
        if enrollment:
            self.overall_progress = enrollment.progress
        self.save()
