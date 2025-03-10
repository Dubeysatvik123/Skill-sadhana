from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from .models import Enrollment, Test, Question, Certification, TestResult, Performance
from .serializers import EnrollmentSerializer, TestSerializer, QuestionSerializer, CertificationSerializer, TestResultSerializer, PerformanceSerializer
from .tasks import send_certificate_email
from .utils import generate_certificate_pdf

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.progress == 100.0:
            instance.is_completed = True
            instance.save()
        
        # Update Performance model
        performance, created = Performance.objects.get_or_create(student=instance.student, course=instance.course)
        performance.update_performance()

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        test_result = serializer.save()
        
        # Update Performance model
        performance, created = Performance.objects.get_or_create(student=test_result.student, course=test_result.test.course)
        performance.update_performance()

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        certificate = serializer.save()
        pdf_path = generate_certificate_pdf(certificate)
        send_certificate_email.delay(certificate.student.email, pdf_path)
        
        # Update Performance model
        performance, created = Performance.objects.get_or_create(student=certificate.student, course=certificate.course)
        performance.update_performance()
        
        return Response({'message': 'Certificate requested and pending admin approval'}, status=status.HTTP_201_CREATED)

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
