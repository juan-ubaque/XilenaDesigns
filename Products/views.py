from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse

from django.views.generic import *
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




#Endpoints de la API
def getCategories(request):

    if request.method == 'GET':
        #categories = serializers.serialize('json', Category.objects.all())
        # categories = list(Category.objects.values())
        categories = [
        {'ID': 1, 'NOMBRE': 'ARETES'},
        {'ID': 2, 'NOMBRE': 'COLLARES'},
        # ... más categorías ...
        ]
    return JsonResponse(categories, safe=False)
