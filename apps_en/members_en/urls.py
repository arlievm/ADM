from django.urls import path
from .views import MembersENListAPIView, MembersENRetrieveAPIView, SponsorENListAPIView, SponsorENRetrieveAPIView, AttributeSponsorsENListAPIView, AttributeSponsorsENRetrieveAPIView

urlpatterns = [
    ######### Преимущества для участников
    path('benefits-members-en/', MembersENListAPIView.as_view()),
    path('benefits-members-en/<int:pk>', MembersENRetrieveAPIView.as_view()),
    #######    Спонсорство
    path('benefits-sponsor-en/', SponsorENListAPIView.as_view()),
    path('benefits-sponsor-en/<int:pk>', SponsorENRetrieveAPIView.as_view()),
    ########    Преимущества для спонсорства
    path('attribute-sponsors-en/', AttributeSponsorsENListAPIView.as_view()),
    path('attribute-sponsors-en/<int:pk>', AttributeSponsorsENRetrieveAPIView.as_view()),
]