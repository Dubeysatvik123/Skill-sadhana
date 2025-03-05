from django.contrib import admin
from django.contrib import admin
from .models import Course, CourseCategory # Remove Enrollment from this list


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'is_approved')
    actions = ['approve_course']

    def approve_course(self, request, queryset):
        queryset.update(is_approved=True)
        for course in queryset:
            send_course_approval_email_task.delay(course.id)

admin.site.register(Course, CourseAdmin)