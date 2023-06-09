from rest_framework import serializers as s

from .models import Location, Stand, Hotel, Feedback, Contacts


class LocationSerializer(s.Serializer):

   class Meta:
       model = Location
       fields = 'category', 'address', 'description', 'location', 'image', 'id'


class HotelSerializar(s.Serializer):

    class Meta:
        model = Hotel
        fields = 'name', 'image', 'description', 'url', 'location', 'id'


class StandSerializer(s.ModelSerializer):

    class Meta:
        model = Stand
        fields = 'status', 'square', 'description', 'price', 'id',


class FeedbackSerializer(s.ModelSerializer):

    class Meta:
        model = Feedback    
        fields = 'name', 'mail', 'phone', 'description', 'id'


class ContactsSerializer(s.ModelSerializer):

    class Meta:
        model = Contacts
        fields = 'phone', 'mail', 'address_ru', 'address_en', 'id'