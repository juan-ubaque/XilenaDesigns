from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.http import JsonResponse

from django.views.generic import *
# Create your views here.

#importamos excepcion para inhabilitar el csrf
from django.views.decorators.csrf import csrf_exempt

#importamos errores 
from django.shortcuts import get_object_or_404

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



def cart(request):
        
        return render(request, 'components/carrito.html')


#Endpoints de la API de categorias
def getCategories(request):
    if request.method == 'GET':
        categories = list(Categories.objects.values())

        data = {
            'categories': categories
        }

        return JsonResponse(data)


def updateCategories(request, id):
    categoria = Categories.objects.get(pk=id)

    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre_categoria')

        if nuevo_nombre:
            categoria.name_categories = nuevo_nombre
            categoria.save()

            return JsonResponse({'ok': True})
        else:
            return JsonResponse({'ok': False, 'error': 'El nombre de la categoría no puede estar vacío'}, status=400)

    return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)



def createCategories(request):

    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre_categoria')

        if nombre_categoria:
            try:
                categoria = Categories(name_categories=nombre_categoria)
                categoria.save()
            except Exception as e:
                return JsonResponse({'ok': False, 'error': 'La categoría ya existe'}, status=400)

            return JsonResponse({'ok': True})
        else:
            return JsonResponse({'ok': False, 'error': 'El proceso de actualización falló'}, status=400)

    return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)


def deleteCategories(request, id):

    if request.method == 'DELETE':
        try:
            categoria = Categories.objects.get(pk=id)
            categoria.delete()
            return JsonResponse({'ok': True})
        except Exception as e:
            return JsonResponse({'ok': False, 'error': 'El proceso de eliminación falló'}, status=400)

    return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)


#Endpoints de la API de productos
def getProducts(request):
    if request.method == 'GET':
        
        # products = list(Product.objects.values('id', 'Product', 'category__', 'description', 'price', 'image'))
        #Consultamos los productos y el nombre de la categoria a la que pertenece
        products = list(Product.objects.values('id', 'Product', 'category__name_categories', 'description', 'price', 'image'))
        data = {
            'products': products
        }

        return JsonResponse(data)
    
