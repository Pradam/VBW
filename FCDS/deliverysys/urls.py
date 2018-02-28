"""Urls for Delivery System Module."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('husks-list/', views.HuskListPage.as_view(), name='husks-list')
]