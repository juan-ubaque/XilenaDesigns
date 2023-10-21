from django.shortcuts import render
from django.http import HttpResponse
from .models import *


from django.views.generic import *
# Create your views here.



#Creamos TemplateView
class HomeListView(TemplateView):

    template_name = 'products/homeProducts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos"] = Product.objects.all()[:5]
        context["categorias"] = Categories.objects.all()

        return context
