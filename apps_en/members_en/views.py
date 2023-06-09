from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import MembersEN, SponsorEN, AttributeSponsorsEN
from .serializers import MembersTwoENSerializer, SponsorENSerializer, AttributeSponsorsENSerializer

#######   Преимущества для участников
class MembersENListAPIView(ListAPIView):
    queryset = MembersEN.objects.all()
    serializer_class = MembersTwoENSerializer
    
    
class MembersENRetrieveAPIView(RetrieveAPIView):
    queryset = MembersEN.objects.all()
    serializer_class = MembersTwoENSerializer

#######    Спонсорство
class SponsorENListAPIView(ListAPIView):
    queryset = SponsorEN.objects.all()
    serializer_class = SponsorENSerializer
    
    
class SponsorENRetrieveAPIView(RetrieveAPIView):
    queryset = SponsorEN.objects.all()
    serializer_class = SponsorENSerializer

#######      Преимущества для спонсорства
class AttributeSponsorsENListAPIView(ListAPIView):
    queryset = AttributeSponsorsEN.objects.all()
    serializer_class = AttributeSponsorsENSerializer
    
    
class AttributeSponsorsENRetrieveAPIView(RetrieveAPIView):
    queryset = AttributeSponsorsEN.objects.all()
    serializer_class = AttributeSponsorsENSerializer