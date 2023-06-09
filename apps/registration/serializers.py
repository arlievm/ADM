from .models import Application
from rest_framework import serializers as s


class ApplicationSerializer(s.ModelSerializer):
    
    class Meta:
        model = Application
        fields = '__all__'
        #  fields = 'name_organic', 'surname', 'name', 'email', 'number', 'user_status', 'id'