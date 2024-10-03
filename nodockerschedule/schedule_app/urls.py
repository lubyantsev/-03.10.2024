"""
URL configuration for schedule_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from schedules import views
from schedules.views import home_view
from schedules.views import home_view, schedules_view, schedule_detail_view


urlpatterns = [
    path('', home_view, name='home'),
    path('create_schedule/', schedules_view, name='schedules_view'),
    path('schedule/<int:schedule_id>/', schedule_detail_view, name='schedule_detail'),
    #path('admin/', admin.site.urls),
    path('home/', views.home_view, name='home'),
    path('schedules/', views.schedules_view, name='schedules'),
    path('', home_view, name='home'),
    path('schedules/', include('schedules.urls')),
]
