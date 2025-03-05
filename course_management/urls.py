from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, CourseApprovalViewSet, ModuleViewSet, 
    VideoContentViewSet, PDFContentViewSet, LiveClassViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course-approvals', CourseApprovalViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'videos', VideoContentViewSet)
router.register(r'pdfs', PDFContentViewSet)
router.register(r'live-classes', LiveClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
