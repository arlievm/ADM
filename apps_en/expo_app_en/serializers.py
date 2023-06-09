from rest_framework import serializers as s

from .models import LocationEn, StandEn, HotelEn


class LocationEnSerializer(s.Serializer):

   class Meta:
       model = LocationEn
       fields = 'category', 'address', 'description', 'location', 'image', 'id'


class HotelEnSerializar(s.Serializer):

    class Meta:
        model = HotelEn
        fields = 'name', 'image', 'description', 'url', 'location', 'id'


class StandEnSerializer(s.ModelSerializer):

    class Meta:
        model = StandEn
        fields = 'status', 'square', 'description', 'price', 'id',
        
        