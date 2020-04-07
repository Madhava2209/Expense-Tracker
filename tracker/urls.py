from django.contrib import admin
from django.urls import path
from tracker.views import *
urlpatterns = [
    path(r^'dashboard/',dashboard),
    path(r^'wallet/',get_all_wallet),
    path(r^'expense/',get_all_expense),
    path(r^'income/',get_all_income),
    path(r^'create_wallet/',create_wallet),
    path(r^'create_income/',create_income),
    path(r^'create_expense/',create_expense),
    path(r^'delete_wallet/<int:wallet_id>/',delete_wallet),
    path(r^'delete_income/<int:income_id>/',delete_income),
    path(r^'delete_expense/<int:expense_id>/',delete_expense),
    path(r^"edit_wallet/<int:wallet_id>/",edit_wallet),
    path(r^"edit_income/<int:income_id>/",edit_income),
    path(r^"edit_expense/<int:expense_id>/",edit_expense),
    
]