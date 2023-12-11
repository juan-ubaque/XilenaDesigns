from django.urls import path

from .views import *


urlpatterns = [
    #--------------------------------- URLS HOME ------------------------------------#      
    path('', HomeListView.as_view(), name='home'),
    path('View/Product/<int:pk>/', ProductDetailView.as_view(), name='ProductDetailView'),
    #--------------------------------- URLS CART ------------------------------------#
    path('cart', CartList, name='cart'),
    path('addCart/<int:id>/', addCart, name='addCart'),
    path('deleteCart/<int:id>/', removeCart, name='deleteItemCart'),
    path('addOneItemCart/<int:id>', addOneItemCart, name='addOneItemCart'),
    path('addInCart/<int:id>', addInCart, name='addInCart'),


    #--------------------------------- URLS CATEGORIES ------------------------------------#
    path('adminCustom/createCategories/', createCategories, name='createCategories'),
    path('adminCustom/getCategories', getCategories, name='getCategories'),
    path('adminCustom/updateCategories/<int:id>/', updateCategories, name='updateCategories'),
    path('adminCustom/deleteCategories/<int:id>/', deleteCategories, name='deleteCategories'),

    
    #--------------------------------- URLS PRODUCTS ------------------------------------#
    path('adminCustom/createProducts/', createProducts, name='createProducts'),
    path('adminCustom/getProducts', getProducts, name='getProducts'),
    path('adminCustom/updateProducts/<int:id>/', updateProducts, name='updateProducts'),
    path('adminCustom/deleteProducts/<int:id>/', deleteProducts, name='deleteProducts'),

    #--------------------------------- URLS SEND MESSAGES ------------------------------------#
    #Envio de mensajes
    path('sendMessage', enviar_mensaje_view, name='sendMessage'),
    #Envio de Correos
    path('sendEmail/<int:id>/', send_email, name='sendEmail'),

    path('test', test, name='test'),




]