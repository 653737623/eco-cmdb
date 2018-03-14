from django.contrib import admin
from django.urls import path, include
from blog import views
from . import  views
urlpatterns=[
    path("login/",views.user_login),
]
