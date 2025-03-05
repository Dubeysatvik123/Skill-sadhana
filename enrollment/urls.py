from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrollmentViewSet, TestViewSet, QuestionViewSet, CertificationViewSet

router = DefaultRouter()
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'certifications', CertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
