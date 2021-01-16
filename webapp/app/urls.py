from django.contrib import admin
from django.urls import path,include
from app import views 

urlpatterns = [
    
    path('', views.home1),
    path('event.html', views.home2),
    path('home.html', views.home1),
    

]