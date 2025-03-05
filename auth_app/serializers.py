from rest_framework import serializers
from .models import User  # Import User model directly

# Allowed roles
VALID_ROLES = ["student", "instructor", "admin"]

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'role', 'unique_id', 'password', 
            'profile_image', 'contact', 'branch', 'institution', 'year', 
            'semester', 'qualification', 'designation', 'experience', 
            'associated_with'
        ]
        extra_kwargs = {'password': {'write_only': True}}  # Hide password in responses

    def validate_email(self, value):
        """Ensure email is unique."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_role(self, value):
        """Ensure role is valid."""
        if value.lower() not in VALID_ROLES:
            raise serializers.ValidationError("Invalid role. Choose from: student, instructor, admin.")
        return value.lower()

    def create(self, validated_data):
        """
        Custom create method to hash passwords properly before saving.
        """
        validated_data['role'] = validated_data.get('role', 'student').lower()  # Default role
        validated_data['is_active'] = False  # Set new users as inactive until admin approval

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Hash password securely
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Ensure password is properly hashed on update.
        """
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))

        return super().update(instance, validated_data)
