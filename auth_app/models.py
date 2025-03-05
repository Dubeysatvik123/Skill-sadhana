from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.hashers import make_password
import uuid

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin')
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    unique_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    experience = models.CharField(max_length=200, null=True, blank=True)
    associated_with = models.CharField(max_length=200, null=True, blank=True)

    # Fix group and permission conflicts
    groups = models.ManyToManyField(Group, related_name="auth_app_users_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="auth_app_users_permissions", blank=True)

    def save(self, *args, **kwargs):
        # Generate unique_id only when user is created
        if not self.unique_id:
            self.unique_id = f"{self.role[:3]}_{uuid.uuid4().hex[:8]}"  # Ensuring uniqueness
        
        # Hash password only if it’s being set for the first time
        if self.pk is None and not self.password.startswith(('pbkdf2_', 'argon2$', 'bcrypt$', 'sha256$')):
            self.password = make_password(self.password)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"
    contact = models.CharField(max_length=15, null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    experience = models.CharField(max_length=200, null=True, blank=True)
    associated_with = models.CharField(max_length=200, null=True, blank=True)

    # Fix group and permission conflicts
    groups = models.ManyToManyField(Group, related_name="auth_app_users_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="auth_app_users_permissions", blank=True)

    def save(self, *args, **kwargs):
        # Generate unique_id only when user is created
        if not self.unique_id:
            self.unique_id = f"{self.role[:3]}_{uuid.uuid4().hex[:8]}"  # Ensuring uniqueness
        
        # Hash password only if it’s being set for the first time
        if self.pk is None and not self.password.startswith(('pbkdf2_', 'argon2$', 'bcrypt$', 'sha256$')):
            self.password = make_password(self.password)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"
