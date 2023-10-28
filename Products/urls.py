from django.urls import path

from .views import *


urlpatterns = [
    
    path('', HomeListView.as_view(), name='home'),

    path('adminCustom/getCategories', getCategories, name='getCategories'),


]