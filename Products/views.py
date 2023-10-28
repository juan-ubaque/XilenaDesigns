from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.http import JsonResponse

from django.views.generic import *
# Create your views here.


def home(request):
    
    productos = Product.objects.all()

    return render(request, 'products/homeProducts.html', {'productos': productos})


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

