from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import LocationEn, StandEn, HotelEn
from .serializers import LocationEnSerializer, StandEnSerializer, HotelEnSerializar

##### Location
class LocationEnListAPIView(ListAPIView):
    queryset = LocationEn.objects.all()
    serializer_class = LocationEnSerializer


class LocationEnRetrieveAPIView(RetrieveAPIView):
    queryset = LocationEn.objects.all()
    serializer_class = LocationEnSerializer

#####   HOTEL
class HotelEnListAPIView(ListAPIView):
    queryset = HotelEn.objects.all()
    serializer_class = HotelEnSerializar


class HotelEnRetrieveAPIView(RetrieveAPIView):
    queryset = HotelEn.objects.all()
    serializer_class = HotelEnSerializar

#### STAND
class StandEnListAPIView(ListAPIView):
    queryset = StandEn.objects.all()
    serializer_class = StandEnSerializer


class StandEnRetrieveAPIView(RetrieveAPIView):
    queryset = StandEn.objects.all()
    serializer_class = StandEnSerializer