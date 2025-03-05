from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.utils.timezone import now
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.signals import user_logged_in

User = get_user_model()

### ✅ Signal 1: Send Welcome Email After Signup
@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Skill Sadhana LMS 🎉"
        message = f"Hi {instance.username},\n\nThank you for signing up! Start exploring courses now."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])

### ✅ Signal 2: Log Last Login Time When User Logs In
@receiver(user_logged_in)
def update_last_login(sender, request, user, **kwargs):
    user.last_login = now()
    user.save()
