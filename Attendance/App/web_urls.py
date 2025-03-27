from django.contrib import admin
from django.urls import path
from . import web_views


urlpatterns = [
    path('',web_views.home, name='home'),
    path('register/', web_views.signUp, name='register'),
    path('login/', web_views.signIn, name='login'),
]