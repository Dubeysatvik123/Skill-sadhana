from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_approval_email(user_email, username, role):
    """
    Sends a confirmation email after admin approves the user.
    """
    subject = "Your Skill Sadhana Account is Approved ✅"
    message = f"Hi {username},\n\nYour {role} account has been approved by the admin. You can now log in and start using Skill Sadhana LMS.\n\nHappy Learning!"
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])

    return f"Approval email sent to {user_email}"
