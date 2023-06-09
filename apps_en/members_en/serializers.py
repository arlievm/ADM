from rest_framework import serializers as s

from .models import MembersEN, SponsorEN, AttributeSponsorsEN


class MembersTwoENSerializer(s.ModelSerializer):
    
    class Meta:
        model = MembersEN
        fields = 'category', 'image', 'title', 'description', 'id'


class SponsorENSerializer(s.ModelSerializer):
    
    class Meta:
        model = SponsorEN
        fields = 'category', 'title', 'description', 'id'


class AttributeSponsorsENSerializer(s.ModelSerializer):

    class Meta:
        model = AttributeSponsorsEN
        fields = 'sponsor', 'image', 'title', 'description', 'id'