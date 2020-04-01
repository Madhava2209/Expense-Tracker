from django.contrib import admin
from django.urls import path
from tracker.views import *
urlpatterns = [
    path('dashboard/',dashboard),
    path('wallet/',get_all_wallet),
    path('expense/',get_all_expense),
    path('income/',get_all_income),
    path('create_wallet/',create_wallet),
    path('create_income/',create_income),
    path('create_expense/',create_expense),

]