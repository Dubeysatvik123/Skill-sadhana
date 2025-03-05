from rest_framework import serializers
from .models import Course, CourseApproval, Module, VideoContent, PDFContent, LiveClass

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseApproval
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = '__all__'

class PDFContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFContent
        fields = '__all__'

class LiveClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveClass
        fields = '__all__'
