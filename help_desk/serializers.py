from rest_framework import serializers
from .models import HelpDeskQuery

class HelpDeskQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpDeskQuery
        fields = '__all__'
