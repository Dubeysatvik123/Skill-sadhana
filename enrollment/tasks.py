from celery import shared_task
from django.core.mail import EmailMessage
import os

@shared_task
def send_certificate_email(email, pdf_path):
    subject = "Your Course Completion Certificate"
    message = "Congratulations! Your certificate is attached."
    email_msg = EmailMessage(subject, message, 'admin@skillsadhana.com', [email])
    email_msg.attach_file(pdf_path)
    email_msg.send()
    os.remove(pdf_path)
