from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from django.contrib import admin
from .views import UserViewSet



router = DefaultRouter()
router.register(r'users', UserViewSet)

app_name = 'auth_app'

urlpatterns = [
    # User Management APIs
    path('', include(router.urls)),

    # Authentication Routes (JWT)
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # Admin Panel (Corrected)
    path('django-admin/', admin.site.urls, name='django_admin'),

    # Admin Approval Route
    path('admin/approve-user/<int:pk>/', UserViewSet.as_view({'post': 'approve_user'}), name='approve-user'),

]

