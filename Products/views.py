from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.


def home(request):
    
    productos = Product.objects.all()

    return render(request, 'index.html', {'productos': productos})



