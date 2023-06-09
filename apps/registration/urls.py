from django.urls import path
from .views import ApplicationCreateListView, ApplicationDeleteView


urlpatterns = [
    ############   Заявка
    path('application/', ApplicationCreateListView.as_view()),
    path('application/<int:pk>', ApplicationDeleteView.as_view()),
]