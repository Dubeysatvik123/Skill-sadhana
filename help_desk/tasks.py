from celery import shared_task
from django.core.mail import send_mail
from .models import HelpDeskQuery

@shared_task
def send_helpdesk_notification(query_id):
    try:
        query = HelpDeskQuery.objects.get(id=query_id)
        send_mail(
            subject="New Help Desk Query Submitted",
            message=f"A new query has been submitted by {query.name}.\n\nQuery:\n{query.query}",
            from_email="admin@skillsadhana.com",
            recipient_list=["admin@skillsadhana.com"],
            fail_silently=False,
        )
    except HelpDeskQuery.DoesNotExist:
        pass
