from django.contrib import admin
from django.urls import path, include
from web_app import views

urlpatterns = [
    path('',views.home, name='home')
    
]
