#--------------------------------- MESSAGES ------------------------------------#

from django.contrib                 import messages
#--------------------------------- VIEWS ------------------------------------#

from django.views.generic           import *
#--------------------------------- SHORCUTS ------------------------------------#

from django.shortcuts               import render, redirect
from django.shortcuts               import get_object_or_404
#--------------------------------- AUTH ------------------------------------#
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms      import UserCreationForm
from django.contrib.auth.forms      import PasswordResetForm
from django.contrib.auth            import authenticate, login, logout
#--------------------------------- URLS ------------------------------------#

from Products.urls                  import urlpatterns
#-------------------------------- MODELS -----------------------------------#

from Products.models                import *
from django.contrib.auth.models     import User






@login_required
def adminHome(request):

    sessionUser = request.session.get('user', None)#obtenemos el usuario de la sesion

    if sessionUser:
        user = User.objects.get(pk=request.user.id)
    else:
        user = None

    context = {
        'user': user,
        'name': user.first_name + ' ' + user.last_name,
    }    

    return render(request, 'adminHome.html', context)


class CategoriesView(TemplateView):
    template_name = "Pages/Categories.html"

class ProductsView(TemplateView):
    template_name = "Pages/Products.html"

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

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            if user.is_superuser:
                request.session['user'] = user.id
                return redirect('adminHome')
            else:
                request.session['user'] = user.id
                # Verificar si el usuario ya tiene un carrito
                cart = Cart.objects.filter(user=user).first()
                
                if not cart:
                    # Crear un carrito para el usuario si no tiene uno
                    cart = Cart(user=user)
                    cart.save()
                
                return redirect('home')
        else:
            return redirect('login')
    
    return render(request, 'registration/login.html')



def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                # Aquí podrías añadir algunos parámetros adicionales si es necesario
                # por ejemplo, email_template_name='my_custom_email_template.html'
            )
            messages.success(request, 'Se ha enviado un correo con instrucciones para restablecer la contraseña.')
            return render(request, 'password_reset_request.html', {'form': form})
        else:
            messages.error(request, 'Ocurrió un error. Por favor, intenta de nuevo.')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/recovery.html', {'form': form})



    
def registrar(request):
    if request.method == 'POST':
        #Recuperar los datos del formulario
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        #Crear el usuario
        user = User.objects.create_user(username=username, password=password, email=email, first_name=nombre, last_name=apellido)
        return redirect('login')  # Redirigir al login después del registro exitoso
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def userLogout(request):

    logout(request)

    return redirect('login')


#--------------------------------- VIEWS ACCOUNT ------------------------------------#
class AccountProfileView(TemplateView):
    template_name = 'Pages/Account/AccountProfile.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Perfil'
        return context


class AccountSecurityView(TemplateView):
    template_name = 'Pages/Account/AccountSecurity.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Seguridad'
        return context

class AccountNotificationsView(TemplateView):
    template_name = 'Pages/Account/AccountNotifications.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notificaciones'
        return context