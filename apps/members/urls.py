from django.urls import path
from .views import MembersListAPIView, MembersRetrieveAPIView, SponsorListAPIView, SponsorRetrieveAPIView, AttributeSponsorsListAPIView, AttributeSponsorsRetrieveAPIView

urlpatterns = [
    ######### Преимущества для участников
    path('benefits-members/', MembersListAPIView.as_view()),
    path('benefits-members/<int:pk>', MembersRetrieveAPIView.as_view()),
    #######    Спонсорство
    path('benefits-sponsor/', SponsorListAPIView.as_view()),
    path('benefits-sponsor/<int:pk>', SponsorRetrieveAPIView.as_view()),
    ########    Преимущества для спонсорства
    path('attribute-sponsors/', AttributeSponsorsListAPIView.as_view()),
    path('attribute-sponsors/<int:pk>', AttributeSponsorsRetrieveAPIView.as_view()),
]