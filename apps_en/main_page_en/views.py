from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import CategoryEN, PageOneEN, MembersEN, ForumEN, TargetEN, TasksEN, EllipseEN, VideoEN, ZoneEN, SectorsEN, PlaceEN, SpeakersEN, OrganizersEN, SponsorsEN, PartnersEN, PlaceOfficeEN, SocialsEN
from .serializers import CategoryENSerializer, PageOneENSerializer, MembersENSerializer, ForumENSerializer, TargetENSerializer, TasksENSerializer, EllipseENSerializer, VideoENSerializer, ZoneENSerializer, \
                            SectorsENSerializer,  PlaceENSerializer, SpeakersENSerializer, OrganizersENSerializer, SponsorsENSerializer, PartnersENSerializer, PlaceOfficeENSerializer, SocialsENSerializer

############   Категория
class CategoryENList(generics.ListAPIView):
    queryset = CategoryEN.objects.filter(parent__isnull=True). \
        select_related('parent'). \
        prefetch_related('children',
                         'children__children',
                         'children__children__children')
    serializer_class = CategoryENSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name',]


class CategoryENRetrieve(generics.RetrieveAPIView):
    queryset = CategoryEN.objects.filter()

    serializer_class = CategoryENSerializer

############ MAIN
class PageOneENListAPIView(ListAPIView):
    queryset = PageOneEN.objects.all()
    serializer_class = PageOneENSerializer
    
    
class PageOneENRetrieveAPIView(RetrieveAPIView):
    queryset = PageOneEN.objects.all()
    serializer_class = PageOneENSerializer

######### Участники 
class MembersENListAPIView(ListAPIView):
    queryset = MembersEN.objects.all()
    serializer_class = MembersENSerializer


class MembersENRetrieveAPIView(RetrieveAPIView):
    queryset = MembersEN.objects.all()
    serializer_class = MembersENSerializer

######### О_форуме
class ForumENListAPIView(ListAPIView):
    queryset = ForumEN.objects.all()
    serializer_class = ForumENSerializer


class ForumENRetrieveAPIView(RetrieveAPIView):
    queryset = ForumEN.objects.all()
    serializer_class = ForumENSerializer

######## ЦЕЛИ
class TargetENListAPIView(ListAPIView):
    queryset = TargetEN.objects.all()
    serializer_class = TargetENSerializer


class TargetENRetriveAPIView(RetrieveAPIView):
    queryset = TargetEN.objects.all()
    serializer_class = TargetENSerializer

####### Задания
class TasksENListAPIView(ListAPIView):
    queryset = TasksEN.objects.all()
    serializer_class = TasksENSerializer


class TasksENRetriveAPIView(RetrieveAPIView):
    queryset = TasksEN.objects.all()
    serializer_class = TasksENSerializer

#######  Элипс
class EllipseENListAPIView(ListAPIView):
    queryset = EllipseEN.objects.all()
    serializer_class = EllipseENSerializer


class EllipseENRetriveAPIView(RetrieveAPIView):
    queryset = EllipseEN.objects.all()
    serializer_class = EllipseENSerializer

######  Видео
class VideoENListAPIView(ListAPIView):
    queryset = VideoEN.objects.all()
    serializer_class = VideoENSerializer


class VideoENRetriveAPIView(RetrieveAPIView):
    queryset = VideoEN.objects.all()
    serializer_class = VideoENSerializer

######  ZONE
class ZoneENListAPIView(ListAPIView):
    queryset = ZoneEN.objects.all()
    serializer_class = ZoneENSerializer


class ZoneENRetriveAPIView(RetrieveAPIView):
    queryset = ZoneEN.objects.all()
    serializer_class = ZoneENSerializer


######   Секторы
class SectorsENListAPIView(ListAPIView):
    queryset = SectorsEN.objects.all()
    serializer_class = SectorsENSerializer


class SectorsENRetriveAPIView(RetrieveAPIView):
    queryset = SectorsEN.objects.all()
    serializer_class = SectorsENSerializer

######  Локации
class PlaceENListAPIView(ListAPIView):
    queryset = PlaceEN.objects.all()
    serializer_class = PlaceENSerializer


class PlaceENRetriveAPIView(RetrieveAPIView):
    queryset = PlaceEN.objects.all()
    serializer_class = PlaceENSerializer

######  Спикеры
class SpeakersENListAPIView(ListAPIView):
    queryset = SpeakersEN.objects.all()
    serializer_class = SpeakersENSerializer


class SpeakersENRetriveAPIView(RetrieveAPIView):
    queryset = SpeakersEN.objects.all()
    serializer_class = SpeakersENSerializer

#######  Организаторы
class OrganizersENListAPIView(ListAPIView):
    queryset = OrganizersEN.objects.all()
    serializer_class = OrganizersENSerializer


class OrganizersENRetriveAPIView(RetrieveAPIView):
    queryset = OrganizersEN.objects.all()
    serializer_class = OrganizersENSerializer

########   Спонсоры
class SponsorsENListAPIView(ListAPIView):
    queryset = SponsorsEN.objects.all()
    serializer_class = SponsorsENSerializer


class SponsorsENRetriveAPIView(RetrieveAPIView):
    queryset = SponsorsEN.objects.all()
    serializer_class = SponsorsENSerializer

#######    Партнеры
class PartnersENListAPIView(ListAPIView):
    queryset = PartnersEN.objects.all()
    serializer_class = PartnersENSerializer


class PartnersENRetriveAPIView(RetrieveAPIView):
    queryset = PartnersEN.objects.all()
    serializer_class = PartnersENSerializer
    
######  Локации офис
class PlaceOfficeENListAPIView(ListAPIView):
    queryset = PlaceOfficeEN.objects.all()
    serializer_class = PlaceOfficeENSerializer


class PlaceOfficeENRetriveAPIView(RetrieveAPIView):
    queryset = PlaceOfficeEN.objects.all()
    serializer_class = PlaceOfficeENSerializer

#######   Социальные сети
class SocialsENListAPIView(ListAPIView):
    queryset = SocialsEN.objects.all()
    serializer_class = SocialsENSerializer


class SocialsENRetriveAPIView(RetrieveAPIView):
    queryset = SocialsEN.objects.all()
    serializer_class = SocialsENSerializer