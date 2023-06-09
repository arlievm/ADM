from .models import CategoryEN, PageOneEN, MembersEN, ForumEN, TargetEN, TasksEN, EllipseEN, VideoEN, ZoneEN, SectorsEN, PlaceEN, SpeakersEN, OrganizersEN, SponsorsEN, PartnersEN, PlaceOfficeEN, SocialsEN
from rest_framework import serializers as s


class RecursiveENSerializer(s.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryENSerializer(s.ModelSerializer):
    children = RecursiveENSerializer(many=True)

    class Meta:
        model = CategoryEN
        fields = 'id', 'name', 'icon', 'image', 'children',
        
        
class PageOneENSerializer(s.ModelSerializer):
    
    class Meta:
        model = PageOneEN
        fields = "__all__"


class MembersENSerializer(s.ModelSerializer):

    class Meta:
        model = MembersEN
        fields = "__all__"


class ForumENSerializer(s.ModelSerializer):
    
    class Meta:
        model = ForumEN
        fields = "__all__"


class TargetENSerializer(s.ModelSerializer):

    class Meta:
        model = TargetEN
        fields = "__all__" 


class TasksENSerializer(s.ModelSerializer):
    class Meta:
        model = TasksEN
        fields = "__all__"


class EllipseENSerializer(s.ModelSerializer):
    
    class Meta:
        model = EllipseEN
        fields = "__all__"


class VideoENSerializer(s.ModelSerializer):

    class Meta:
        model = VideoEN
        fields = "__all__"


class ZoneENSerializer(s.ModelSerializer):

    class Meta:
        model = ZoneEN
        fields = "__all__"


class SectorsENSerializer(s.ModelSerializer):
    
    class Meta:
        model = SectorsEN
        fields = "__all__"


class PlaceENSerializer(s.ModelSerializer):
    
    class Meta:
        model = PlaceEN
        fields = "__all__"


class SpeakersENSerializer(s.ModelSerializer):
    
    class Meta:
        model = SpeakersEN
        fields = "__all__"


class OrganizersENSerializer(s.ModelSerializer):
    
    class Meta:
        model = OrganizersEN
        fields = "__all__"


class SponsorsENSerializer(s.ModelSerializer):

    class Meta:
        model = SponsorsEN
        fields = "__all__"


class SponsorsENSerializer(s.ModelSerializer):
    
    class Meta:
        model = SpeakersEN
        fields = "__all__"


class PartnersENSerializer(s.ModelSerializer):
    
    class Meta:
        model = PartnersEN
        fields = "__all__"
        
        
class PlaceOfficeENSerializer(s.ModelSerializer):
    
    class Meta:
        model = PlaceOfficeEN
        fields = "__all__"


class SocialsENSerializer(s.ModelSerializer):
    
    class Meta:
        model = SocialsEN
        fields = "__all__"