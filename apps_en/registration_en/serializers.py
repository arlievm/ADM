from rest_framework import serializers as s

from .models import ApplicationEN

class ApplicationENSerializer(s.ModelSerializer):
    
    class Meta:
        model = ApplicationEN
        fields = 'name_organic', 'surname', 'name', 'email', 'number', 'user_status', 'id'