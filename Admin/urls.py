from django.urls import path

from .views import *


urlpatterns = [
    
    path('adminCustom/home', adminHome, name='adminHome'),
]