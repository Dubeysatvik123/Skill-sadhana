from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiscussionForumViewSet, DiscussionCommentViewSet

router = DefaultRouter()
router.register(r'forums', DiscussionForumViewSet)
router.register(r'comments', DiscussionCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

