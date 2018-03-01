"""Urls for Delivery System Module."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('husks-list/', views.HuskListPage.as_view(), name='husks-list'),
    path('coal-list/', views.CoalPageList.as_view(), name='coal-list'),
    path('husk-add/', views.HuskAddPage.as_view(), name='husk-add')
]
