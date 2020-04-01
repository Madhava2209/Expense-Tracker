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
    path('delete_wallet/<int:wallet_id>/',delete_wallet),
    path('delete_income/<int:income_id>/',delete_income),
    path('delete_expense/<int:expense_id>/',delete_expense),
    path("edit_wallet/<int:wallet_id>/",edit_wallet),
    path("edit_income/<int:income_id>/",edit_income),
    path("edit_expense/<int:expense_id>/",edit_expense),
    
]