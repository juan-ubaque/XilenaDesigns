from django.urls import path

from .views import *


urlpatterns = [
    
    path('adminCustom/', adminHome, name='adminHome'),
    
    path('accounts/login/', LoginUser, name='login'),
    path('accounts/logout/', userLogout, name='logout'),
    



]