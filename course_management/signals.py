from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import CourseApproval

@receiver(post_save, sender=CourseApproval)
def send_course_approval_email(sender, instance, created, **kwargs):
    """ Sends an email notification to the instructor on course approval/rejection """
    if not created:
        subject = "Course Approval Update"
        if instance.is_approved:
            message = f"Your course '{instance.course.name}' has been approved. You can now upload content."
        else:
            message = f"Your course '{instance.course.name}' has been rejected. Please contact admin for details."
        
        send_mail(
            subject,
            message,
            'admin@yourlms.com',
            [instance.course.instructor.email],
            fail_silently=False,
        )
