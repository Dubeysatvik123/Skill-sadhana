from rest_framework import viewsets
from .models import Course, CourseApproval, Module, VideoContent, PDFContent, LiveClass
from .serializers import (
    CourseSerializer, CourseApprovalSerializer, 
    ModuleSerializer, VideoContentSerializer, PDFContentSerializer, LiveClassSerializer
)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseApprovalViewSet(viewsets.ModelViewSet):
    queryset = CourseApproval.objects.all()
    serializer_class = CourseApprovalSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class VideoContentViewSet(viewsets.ModelViewSet):
    queryset = VideoContent.objects.all()
    serializer_class = VideoContentSerializer

class PDFContentViewSet(viewsets.ModelViewSet):
    queryset = PDFContent.objects.all()
    serializer_class = PDFContentSerializer

class LiveClassViewSet(viewsets.ModelViewSet):
    queryset = LiveClass.objects.all()
    serializer_class = LiveClassSerializer
