from django.urls import path

from .views import *


urlpatterns = [
    
    path('', HomeListView.as_view(), name='home'),

    
    path('cart', cart, name='cart'),

    # Categorias CRUD
    path('adminCustom/createCategories/', createCategories, name='createCategories'),
    path('adminCustom/getCategories', getCategories, name='getCategories'),
    path('adminCustom/updateCategories/<int:id>/', updateCategories, name='updateCategories'),
    path('adminCustom/deleteCategories/<int:id>/', deleteCategories, name='deleteCategories'),

    # Productos CRUD
    # path('adminCustom/createProducts/', createProducts, name='createProducts'),
    path('adminCustom/getProducts', getProducts, name='getProducts'),
    # path('adminCustom/updateProducts/<int:id>/', updateProducts, name='updateProducts'),
    # path('adminCustom/deleteProducts/<int:id>/', deleteProducts, name='deleteProducts'),



]