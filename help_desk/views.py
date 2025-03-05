from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.mail import send_mail
from .models import HelpDeskQuery
from .serializers import HelpDeskQuerySerializer

class HelpDeskQueryViewSet(viewsets.ModelViewSet):
    queryset = HelpDeskQuery.objects.all().order_by('-created_at')
    serializer_class = HelpDeskQuerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can submit, only authenticated users can view

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            query = serializer.save()
            
            # Send an email notification to the Application Admin
            send_mail(
                subject="New Help Desk Query Submitted",
                message=f"A new help desk query has been submitted by {query.name}.\n\nQuery:\n{query.query}",
                from_email="admin@skillsadhana.com",
                recipient_list=["admin@skillsadhana.com"],  # Change to the real admin email
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
