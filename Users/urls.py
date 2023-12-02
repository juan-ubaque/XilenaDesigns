from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('accounts/register/', UserRegisterView.as_view(), name='register'),
    path('accounts/logintest/', UserLoginView.as_view(), name='testLogin'),
    

]