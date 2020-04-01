from django.contrib import admin
from django.urls import path
from authentication.views import *
urlpatterns = [
    path('signup/',signup),
    path('login/',user_login),
    path('logout/',user_logout),
]