from django.urls import path
from .views import ApplicationENCreateListView, ApplicationENDeleteView


urlpatterns = [
    ############   Заявка
    path('application-en/', ApplicationENCreateListView.as_view()),
    path('application-en/<int:pk>', ApplicationENDeleteView.as_view()),
]