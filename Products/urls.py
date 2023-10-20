from django.urls import path

from .views import *


urlpatterns = [
    
    path('', home, name='home'),
    path('test', homeTest, name='test'),
    path('list', HomeListView.as_view(), name='list'),

]