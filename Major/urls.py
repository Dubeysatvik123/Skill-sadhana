from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # Authentication & User Management APIs
    path('api/v1/auth/', include('auth_app.urls')),  

    # Course Management (Course + Content)
    path('api/v1/courses/', include('course_management.urls')),  

    # Enrollment & Certification
    path('api/v1/enrollment/', include('enrollment.urls')),  

    # Discussion Forum
    path('api/v1/forum/', include('discussion.urls')),  

    # Help Desk / Support
    path('api/v1/helpdesk/', include('help_desk.urls')),  
]
