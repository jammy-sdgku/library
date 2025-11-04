from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inventory_page, name='inventory'),
    path('add/', views.inventory_add, name='add'),
    path('inventory/edit/<int:book_id>/', views.inventory_edit, name='edit'),
    path('delete/<int:book_id>/', views.inventory_delete, name='delete'),
]