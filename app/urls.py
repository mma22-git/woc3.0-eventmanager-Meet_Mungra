from django.contrib import admin
from django.urls import path,include
from app import views 

urlpatterns = [
    
    path('', views.home),
    path('home.html', views.home),
    path('event.html', views.event),
    path('part.html', views.part),
    path('dashboard.html', views.dashboard),
    
    ]