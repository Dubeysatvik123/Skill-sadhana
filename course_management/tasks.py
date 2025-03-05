from celery import shared_task

@shared_task
def send_course_approval_email_task(course_id):
    course = Course.objects.get(id=course_id)
    send_mail(
        'Course Approved ✅',
        f'Congratulations! Your course "{course.name}" has been approved and is now live on the platform.',
        'admin@skillsadhana.com',
        [course.instructor.email]
    )

@shared_task
def send_course_rejection_email_task(course_id, rejection_reason):
    course = Course.objects.get(id=course_id)
    send_mail(
        'Course Rejected ❌',
        f'Sorry, your course "{course.name}" has been rejected.\n\nReason: {rejection_reason}',
        'admin@skillsadhana.com',
        [course.instructor.email]
    )
