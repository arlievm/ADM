from django.urls import path
from .views import LocationEnListAPIView, LocationEnRetrieveAPIView, StandEnListAPIView, StandEnRetrieveAPIView, HotelEnListAPIView, HotelEnRetrieveAPIView

urlpatterns = [
    ############   LOCATIONS
    path('location-en/', LocationEnListAPIView.as_view()),
    path('location-en/<int:pk>', LocationEnRetrieveAPIView.as_view()),
    ############   HOTEL
    path('hotel-en/', HotelEnListAPIView.as_view()),
    path('hotel-en/<int:pk>', HotelEnRetrieveAPIView.as_view()),
    ############   STAND
    path('stand-en/', StandEnListAPIView.as_view()),
    path('stand-en/<int:pk>', StandEnRetrieveAPIView.as_view()),
]