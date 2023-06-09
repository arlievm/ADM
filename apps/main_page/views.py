from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category, PageOne, Members, Forum, Target, Tasks, Ellipse, Video, Sectors, Place, Speakers, Organizers, Sponsors, Partners, PlaceOffice, Socials
from .serializers import CategorySerializer, PageOneSerializer, MembersSerializer, ForumSerializer, TargetSerializer, TasksSerializer, EllipseSerializer, VideoSerializer, \
                            SectorsSerializer,  PlaceSerializer, SpeakersSerializer, OrganizersSerializer, SponsorsSerializer, PartnersSerializer, PlaceOfficeSerializer, SocialsSerializer

############   Категория
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True). \
        select_related('parent'). \
        prefetch_related('children',
                         'children__children',
                         'children__children__children')
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name',]


class CategoryRetrieve(generics.RetrieveAPIView):
    queryset = Category.objects.filter()

    serializer_class = CategorySerializer

############ MAIN
class PageOneListAPIView(ListAPIView):
    queryset = PageOne.objects.all()
    serializer_class = PageOneSerializer
    
    
class PageOneRetrieveAPIView(RetrieveAPIView):
    queryset = PageOne.objects.all()
    serializer_class = PageOneSerializer

######### Участники 
class MembersListAPIView(ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class MembersRetrieveAPIView(RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

######### О_форуме
class ForumListAPIView(ListAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer


class ForumRetrieveAPIView(RetrieveAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

######## ЦЕЛИ
class TargetListAPIView(ListAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class TargetRetriveAPIView(RetrieveAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

####### Задания
class TasksListAPIView(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksRetriveAPIView(RetrieveAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

#######  Элипс
class EllipseListAPIView(ListAPIView):
    queryset = Ellipse.objects.all()
    serializer_class = EllipseSerializer


class EllipseRetriveAPIView(RetrieveAPIView):
    queryset = Ellipse.objects.all()
    serializer_class = EllipseSerializer

######  Видео
class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoRetriveAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


######   Секторы
class SectorsListAPIView(ListAPIView):
    queryset = Sectors.objects.all()
    serializer_class = SectorsSerializer


class SectorsRetriveAPIView(RetrieveAPIView):
    queryset = Sectors.objects.all()
    serializer_class = SectorsSerializer

######  Локации
class PlaceListAPIView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceRetriveAPIView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

######  Спикеры
class SpeakersListAPIView(ListAPIView):
    queryset = Speakers.objects.all()
    serializer_class = SpeakersSerializer


class SpeakersRetriveAPIView(RetrieveAPIView):
    queryset = Speakers.objects.all()
    serializer_class = SpeakersSerializer

#######  Организаторы
class OrganizersListAPIView(ListAPIView):
    queryset = Organizers.objects.all()
    serializer_class = OrganizersSerializer


class OrganizersRetriveAPIView(RetrieveAPIView):
    queryset = Organizers.objects.all()
    serializer_class = OrganizersSerializer

########   Спонсоры
class SponsorsListAPIView(ListAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer


class SponsorsRetriveAPIView(RetrieveAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer

#######    Партнеры
class PartnersListAPIView(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer


class PartnersRetriveAPIView(RetrieveAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    
######  Локации офис
class PlaceOfficeListAPIView(ListAPIView):
    queryset = PlaceOffice.objects.all()
    serializer_class = PlaceOfficeSerializer


class PlaceOfficeRetriveAPIView(RetrieveAPIView):
    queryset = PlaceOffice.objects.all()
    serializer_class = PlaceOfficeSerializer
    

#######   Социальные сети
class SocialsListAPIView(ListAPIView):
    queryset = Socials.objects.all()
    serializer_class = SocialsSerializer


class SocialsRetriveAPIView(RetrieveAPIView):
    queryset = Socials.objects.all()
    serializer_class = SocialsSerializer