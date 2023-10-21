from django.urls import path

from .views import *


urlpatterns = [
    
    path('adminCustom/', adminHome, name='adminHome'),
    
    path('login/', LoginUser, name='login'),
    path('logout/', logout, name='logout'),
    

]