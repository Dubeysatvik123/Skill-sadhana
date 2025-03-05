from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelpDeskQueryViewSet

router = DefaultRouter()
router.register(r'helpdesk', HelpDeskQueryViewSet, basename='helpdesk')

urlpatterns = [
    path('', include(router.urls)),

]

