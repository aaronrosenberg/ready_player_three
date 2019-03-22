from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = "app_one"

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^special/$', views.special, name='user_special'),
]
