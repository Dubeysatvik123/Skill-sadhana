from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import DiscussionForum, DiscussionComment
from .serializers import DiscussionForumSerializer, DiscussionCommentSerializer

class DiscussionForumViewSet(viewsets.ModelViewSet):
    queryset = DiscussionForum.objects.all()
    serializer_class = DiscussionForumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        discussion = serializer.save(student=self.request.user)
        # Notify all enrolled students
        enrolled_students = [enrollment.student.email for enrollment in discussion.course.enrollment_set.all()]
        send_mail(
            "New Discussion Created",
            f"A new discussion titled '{discussion.title}' has been created for {discussion.course.name}.",
            "admin@skillsadhana.com",
            enrolled_students,
            fail_silently=False
        )

class DiscussionCommentViewSet(viewsets.ModelViewSet):
    queryset = DiscussionComment.objects.all()
    serializer_class = DiscussionCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
