from django.urls import path
from .views import home, create_schedule, schedule_detail
from . import views
from .views import home_view, schedules_view, schedule_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create_schedule/', schedules_view, name='schedules_view'),
    path('schedule/<int:schedule_id>/', schedule_detail_view, name='schedule_detail'),
    path('home/', views.home, name='home'),
    path('schedules/', views.create_schedule, name='schedules'),
    path('', home, name='home'),  # Главная страница
    path('create/', create_schedule, name='create_schedule'),
    path('<int:schedule_id>/', schedule_detail, name='schedule_detail'),
    path('home/', home_view, name='home'),  # Также можно оставить этот путь
]