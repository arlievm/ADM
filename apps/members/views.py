from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Members, Sponsor, AttributeSponsors
from .serializers import MembersTwoSerializer, SponsorSerializer, AttributeSponsorsSerializer

#######   Преимущества для участников
class MembersListAPIView(ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersTwoSerializer
    
    
class MembersRetrieveAPIView(RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersTwoSerializer

#######    Спонсорство
class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    
    
class SponsorRetrieveAPIView(RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

#######      Преимущества для спонсорства
class AttributeSponsorsListAPIView(ListAPIView):
    queryset = AttributeSponsors.objects.all()
    serializer_class = AttributeSponsorsSerializer
    
    
class AttributeSponsorsRetrieveAPIView(RetrieveAPIView):
    queryset = AttributeSponsors.objects.all()
    serializer_class = AttributeSponsorsSerializer