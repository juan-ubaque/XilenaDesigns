from django.urls import path

from .views import *


urlpatterns = [
    #Principal
    path('', adminHome, name='adminHome'),
    path('AccountSettings/', AccountSettingsView.as_view(), name='AccountSettingsView'),
    #Categorias
    path('View/Categories/', CategoriesView.as_view(), name='CategoriesView'),
    path('View/Products/', ProductsView.as_view(), name='ProductsView'),

    #Autenticacion
    path('accounts/login/', LoginUser, name='login'),
    path('accounts/logout/', userLogout, name='logout'),
    
    path('accounts/recovery/', password_reset_request, name='recovery'),

    #--------------------------------- ACCOUNT ------------------------------------#
    path('accounts/View/Profile',AccountProfileView.as_view(), name='accountProfileView'),
    path('accounts/View/Security',AccountSecurityView.as_view(), name='accountSecurityView'),
    path('accounts/View/Notifications',AccountNotificationsView.as_view(), name='accountNotificationsView'),
]