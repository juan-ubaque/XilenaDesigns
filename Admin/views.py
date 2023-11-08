from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import *

#importamos las urls de la app products
from Products.urls import urlpatterns

#importamos los modelos
from Products.models import *



@login_required
def adminHome(request):

    user = request.session.get('user', None)#obtenemos el usuario de la sesion


    return render(request, 'adminHome.html', {'user': user})


class CategoriesView(TemplateView):
    template_name = "dashboard/Pages/categories.html"

class ProductsView(TemplateView):
    template_name = "dashboard/Pages/Products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categories.objects.all()

        return context




class AccountSettingsView(TemplateView):
    template_name = 'dashboard/Pages/Account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Configuracion de Cuenta'
        return context



def LoginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate (username=username, password=password)

        #Enviamos los datos a mostrar en el template del usuario
       

        if user is not None:
            login(request, user)
            if user.is_superuser:
                request.session['user'] = user.username
                return redirect('adminHome')  # Redirigir al adminHome
            else:
                return redirect('home')

        else:#si no es valido el usuario redirigir a login
            return redirect('login')
    return render(request, 'registration/login.html')



def userLogout(request):

    logout(request)

    return redirect('login')



