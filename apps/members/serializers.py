from rest_framework import serializers as s

from .models import Members, Sponsor, AttributeSponsors


class MembersTwoSerializer(s.ModelSerializer):
    
    class Meta:
        model = Members
        fields = 'category', 'image', 'title', 'description', 'id'


class SponsorSerializer(s.ModelSerializer):
    
    class Meta:
        model = Sponsor
        fields = 'category', 'title', 'description', 'id'


class AttributeSponsorsSerializer(s.ModelSerializer):

    class Meta:
        model = AttributeSponsors
        fields = 'sponsor', 'image', 'title', 'description', 'id'