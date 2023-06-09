from .models import Category, PageOne, Members, Forum, Target, Tasks, Ellipse, Video, Sectors, Place, Speakers, Organizers, Sponsors, Partners, PlaceOffice, Socials
from rest_framework import serializers as s


class RecursiveSerializer(s.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(s.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Category
        fields = 'id', 'name', 'icon', 'image', 'children',
        
        
class PageOneSerializer(s.ModelSerializer):
    
    class Meta:
        model = PageOne
        fields = "__all__"


class MembersSerializer(s.ModelSerializer):

    class Meta:
        model = Members
        fields = "__all__"


class ForumSerializer(s.ModelSerializer):
    
    class Meta:
        model = Forum
        fields = "__all__"


class TargetSerializer(s.ModelSerializer):

    class Meta:
        model = Target
        fields = "__all__" 


class TasksSerializer(s.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class EllipseSerializer(s.ModelSerializer):
    
    class Meta:
        model = Ellipse
        fields = "__all__"


class VideoSerializer(s.ModelSerializer):

    class Meta:
        model = Video
        fields = "__all__"

class SectorsSerializer(s.ModelSerializer):
    
    class Meta:
        model = Sectors
        fields = "__all__"


class PlaceSerializer(s.ModelSerializer):
    
    class Meta:
        model = Place
        fields = "__all__"


class SpeakersSerializer(s.ModelSerializer):
    
    class Meta:
        model = Speakers
        fields = "__all__"


class OrganizersSerializer(s.ModelSerializer):
    
    class Meta:
        model = Organizers
        fields = "__all__"


class SponsorsSerializer(s.ModelSerializer):

    class Meta:
        model = Sponsors
        fields = "__all__"


class SponsorsSerializer(s.ModelSerializer):
    
    class Meta:
        model = Speakers
        fields = "__all__"


class PartnersSerializer(s.ModelSerializer):
    
    class Meta:
        model = Partners
        fields = "__all__"
        
        
class PlaceOfficeSerializer(s.ModelSerializer):
    
    class Meta:
        model = PlaceOffice
        fields = "__all__"


class SocialsSerializer(s.ModelSerializer):
    
    class Meta:
        model = Socials
        fields = "__all__"