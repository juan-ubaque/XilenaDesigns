from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

#Importamos la vista generica ListView
from django.views.generic import ListView
# Create your views here.


def home(request):
    
    productos = Product.objects.all()

    return render(request, 'products/homeProducts.html', {'productos': productos})

def homeTest(request):
    
    productos = Product.objects.all()

    return render(request, 'test.html', {'productos': productos})



#Creamos una listView
class HomeListView(ListView):
    model = Product
    template_name = 'products/homeProducts.html'
    context_object_name = 'productos'
    paginate_by = 5




