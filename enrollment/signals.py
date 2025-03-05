from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Certification

@receiver(post_save, sender=Certification)
def certification_approval(sender, instance, created, **kwargs):
    if not created:
        if instance.is_approved:
            send_mail(
                'Certificate Approved',
                'Your certification request has been approved.',
                'admin@skillsadhana.com',
                [instance.student.email],
                fail_silently=False,
            )
        else:
            send_mail(
                'Certificate Rejected',
                'Your certification request has been rejected.',
                'admin@skillsadhana.com',
                [instance.student.email],
                fail_silently=False,
            )
