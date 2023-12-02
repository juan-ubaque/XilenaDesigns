from django.shortcuts import render,redirect

#Views
from django.views.generic import *
from django.contrib.auth.models import User


#Enviar Correo
from .Email import Email


#Render
from django.template.loader import render_to_string


#Login
class UserRegisterView(View):
    def get(self,request):
        
        return render(request,'registration/register.html')
    
    def post(self,request):
        
        username    = request.POST['username']
        password    = request.POST['password']
        email       = request.POST['email']
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        
        try:
            user = User.objects.create_user(
                username    = username,
                password    = password,
                email       = email,
                first_name  = first_name,
                last_name   = last_name,
                is_staff   = False,
                )
                
            user.save()
            
            #Enviamos el correo de confirmacion
            email = Email()
            email.send_email(
                to      = email,
                Cc      = '',
                subject = 'Confirmacion de Registro',
                message = f'<h1>Confirmacion de Registro</h1><br><p>Gracias por registrarte en nuestro sitio web</p>',
                )


            return redirect('login')
        except:
            
            return redirect('register')


class UserLoginView(View):
    def get(self,request):
        
        return render(request,'registration/loginTest.html')
    
    def post(self,request):
        
        username    = request.POST['username']
        password    = request.POST['password']
        
        try:
            user = authenticate(
                username    = username,
                password    = password,
                )
                
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        except:
            
            return redirect('login')