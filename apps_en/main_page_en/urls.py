from django.urls import path
from apps_en.main_page_en import views

urlpatterns = [
    ############   Категория
    path('category_en/', views.CategoryENList.as_view()),
    path('category_en/<int:pk>', views.CategoryENRetrieve.as_view()),
    ############ MAIN
    path('main-page_en/', views.PageOneENListAPIView.as_view()),
    path('main-page_en/<int:pk>', views.PageOneENRetrieveAPIView.as_view()),
    ######### Участники 
    path('members_en/', views.MembersENListAPIView.as_view()),
    path('members_en/<int:pk>', views.MembersENRetrieveAPIView.as_view()),
    ######### О_форуме
    path('forum_en/', views.ForumENListAPIView.as_view()),
    path('forum_en/<int:pk>', views.ForumENRetrieveAPIView.as_view()),
    ######## ЦЕЛИ
    path('target_en/', views.TargetENListAPIView.as_view()),
    path('target_en/<int:pk>', views.TargetENRetriveAPIView.as_view()),
    ####### Задания
    path('tasks_en/', views.TasksENListAPIView.as_view()),
    path('tasks_en/<int:pk>', views.TasksENRetriveAPIView.as_view()),
    #######  Элипс
    path('ellipse_en/', views.EllipseENListAPIView.as_view()),
    path('ellipse_en/<int:pk>', views.EllipseENRetriveAPIView.as_view()),
    ######  Видео
    path('video_en/', views.VideoENListAPIView.as_view()),
    path('video_en/<int:pk>', views.VideoENRetriveAPIView.as_view()),
    ######   ZONE
    path('zone_en/', views.ZoneENListAPIView.as_view()),
    path('zone_en/<int:pk>', views.ZoneENRetriveAPIView.as_view()),
    ######   Секторы
    path('sectors_en/', views.SectorsENListAPIView.as_view()),
    path('sectors_en/<int:pk>', views.SectorsENListAPIView.as_view()),
    ######  Локации
    path('place_en/', views.PlaceENListAPIView.as_view()),
    path('place_en/<int:pk>', views.PlaceENListAPIView.as_view()),
    ######  Спикеры
    path('speakers_en/', views.SpeakersENListAPIView.as_view()),
    path('speakers_en/<int:pk>', views.SpeakersENRetriveAPIView.as_view()),
    #######  Организаторы
    path('organizers_en/', views.OrganizersENListAPIView.as_view()),
    path('organizers_en/<int:pk>', views.OrganizersENRetriveAPIView.as_view()),
    ########   Спонсоры
    path('sponsors_en/', views.SponsorsENListAPIView.as_view()),
    path('sponsors_en/<int:pk>', views.SponsorsENRetriveAPIView.as_view()),
    #######    Партнеры
    path('partners_en/', views.PartnersENListAPIView.as_view()),
    path('partners_en/<int:pk>', views.PartnersENRetriveAPIView.as_view()),
    ######  Локации офис
    path('place-office_en/', views.PlaceOfficeENListAPIView.as_view()),
    path('place-office_en/<int:pk>', views.PlaceOfficeENRetriveAPIView.as_view()),
    #######   Социальные сети
    path('socials_en/', views.SocialsENListAPIView.as_view()),
    path('socials_en/<int:pk>', views.SocialsENRetriveAPIView.as_view()),
]