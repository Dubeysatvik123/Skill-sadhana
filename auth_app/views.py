from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from .serializers import UserSerializer
from .tasks import send_approval_email  # Celery task for async emails

VALID_ROLES = ["student", "instructor", "admin"]  # Allowed roles

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Signup & login open

    def create(self, request, *args, **kwargs):
        """
        Handles User Signup & Sends Email for Admin Approval.
        """
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        role = request.data.get("role", "student").lower()

        if role not in VALID_ROLES:
            return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already in use"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User(username=username, email=email, role=role, is_active=False)  # Pending approval
        user.set_password(password)  # Hash Password
        user.save()

        # Notify Admins for Approval
        admin_emails = settings.ADMIN_EMAILS  # List of admin emails
        send_mail(
            "Account Approval Required",
            f"A new {role} ({username}) signed up and requires approval.",
            settings.DEFAULT_FROM_EMAIL,
            admin_emails,
        )

        return Response(
            {"message": "Signup successful. Awaiting admin approval."},
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["post"])
    def login(self, request):
        """
        Handles User Login & JWT Token Generation.
        """
        username = request.data.get("username")
        password = request.data.get("password")

        user = get_object_or_404(User, username=username)

        if not user.check_password(password):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({"error": "Account pending admin approval"}, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user_id": user.id,
                "username": user.username,
                "role": user.role,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        )

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAdminUser])
    def approve_user(self, request, pk=None):
        """
        Admin Approves User & Sends Confirmation Email.
        """
        user = get_object_or_404(User, pk=pk)

        if user.is_active:
            return Response({"message": "User already approved"}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()

        # Send Confirmation Email via Celery
        send_approval_email.delay(user.email, user.username, user.role)

        return Response({"message": "User approved & confirmation email sent!"}, status=status.HTTP_200_OK)
