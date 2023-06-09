from django.urls import path
from apps.main_page import views

urlpatterns = [
    ############   Категория
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryRetrieve.as_view()),
    ############ MAIN
    path('main-page/', views.PageOneListAPIView.as_view()),
    path('main-page/<int:pk>', views.PageOneRetrieveAPIView.as_view()),
    ######### Участники 
    path('members/', views.MembersListAPIView.as_view()),
    path('members/<int:pk>', views.MembersRetrieveAPIView.as_view()),
    ######### О_форуме
    path('forum/', views.ForumListAPIView.as_view()),
    path('forum/<int:pk>', views.ForumRetrieveAPIView.as_view()),
    ######## ЦЕЛИ
    path('target/', views.TargetListAPIView.as_view()),
    path('target/<int:pk>', views.TargetRetriveAPIView.as_view()),
    ####### Задания
    path('tasks/', views.TasksListAPIView.as_view()),
    path('tasks/<int:pk>', views.TasksRetriveAPIView.as_view()),
    #######  Элипс
    path('ellipse/', views.EllipseListAPIView.as_view()),
    path('ellipse/<int:pk>', views.EllipseRetriveAPIView.as_view()),
    ######  Видео
    path('video/', views.VideoListAPIView.as_view()),
    path('video/<int:pk>', views.VideoRetriveAPIView.as_view()),
    ######   Секторы
    path('sectors/', views.SectorsListAPIView.as_view()),
    path('sectors/<int:pk>', views.SectorsListAPIView.as_view()),
    ######  Локации
    path('place/', views.PlaceListAPIView.as_view()),
    path('place/<int:pk>', views.PlaceListAPIView.as_view()),
    ######  Спикеры
    path('speakers/', views.SpeakersListAPIView.as_view()),
    path('speakers/<int:pk>', views.SpeakersRetriveAPIView.as_view()),
    #######  Организаторы
    path('organizers/', views.OrganizersListAPIView.as_view()),
    path('organizers/<int:pk>', views.OrganizersRetriveAPIView.as_view()),
    ########   Спонсоры
    path('sponsors/', views.SponsorsListAPIView.as_view()),
    path('sponsors/<int:pk>', views.SponsorsRetriveAPIView.as_view()),
    #######    Партнеры
    path('partners/', views.PartnersListAPIView.as_view()),
    path('partners/<int:pk>', views.PartnersRetriveAPIView.as_view()),
    ######  Локации офис
    path('place-office/', views.PlaceOfficeListAPIView.as_view()),
    path('place-office/<int:pk>', views.PlaceOfficeRetriveAPIView.as_view()),
    #######   Социальные сети
    path('socials/', views.SocialsListAPIView.as_view()),
    path('socials/<int:pk>', views.SocialsRetriveAPIView.as_view()),
]