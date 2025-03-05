from rest_framework import serializers
from .models import DiscussionForum, DiscussionComment

class DiscussionForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionForum
        fields = '__all__'

class DiscussionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionComment
        fields = '__all__'
