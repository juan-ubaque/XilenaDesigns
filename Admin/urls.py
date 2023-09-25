from django.urls import path

from .views import *


urlpatterns = [
    
    path('adminCustom', adminHome, name='adminHome'),
]