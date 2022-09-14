from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('link',views.link,name='link'),
    path('api2',views.api2,name='api2')
]
