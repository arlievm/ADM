from django.shortcuts import render
from rest_framework import generics

from .serializers import ApplicationENSerializer
from .models import ApplicationEN


class ApplicationENCreateListView(generics.ListCreateAPIView):
    queryset = ApplicationEN.objects.all()
    serializer_class = ApplicationENSerializer
    
    
    
class ApplicationENDeleteView(generics.DestroyAPIView):
    queryset = ApplicationEN.objects.all()
    serializer_class = ApplicationENSerializer
    