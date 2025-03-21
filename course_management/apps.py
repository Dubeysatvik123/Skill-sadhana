from django.apps import AppConfig

class CourseManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course_management'

    def ready(self):
        import course_management.signals
