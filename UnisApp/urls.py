from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from UnisApp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', views.profiles, name='account'),
]
