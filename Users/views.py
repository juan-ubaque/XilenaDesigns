from django.shortcuts import render,redirect

#Views
from django.views.generic import *
from django.contrib.auth.models import User


#Enviar Correo
from ASSETS.Email import Email


#Render
from django.template.loader import render_to_string

#Settings
from django.conf import settings


#--------------------------------- VIEWS AUTH ------------------------------------#
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

            #comprobamos que el usuario no exista
            if User.objects.filter(username=username).exists():
                return redirect('register')

            user = User.objects.create_user(
                username    = username,
                password    = password,
                email       = email,
                first_name  = first_name,
                last_name   = last_name,
                is_staff    = False,
                )
            user.save()
            
            #Enviamos el correo de confirmacion
            email = Email(
                email    = settings.EMAIL_HOST_USER,
                password = settings.EMAIL_HOST_PASSWORD,
            )

            #Adjuntamos las imagenes
            listImages = [
                'static/img/LogoXilena.jpg',
                'static/img/images_mail/Email.png',
                'static/img/images_mail/Regalo.png',
                'static/img/images_mail/facebook2x.png',
                'static/img/images_mail/instagram2x.png',
            ]
            listName = [
                'LogoXilena',
                'ImgEmail',
                'regalo',
                'ImgFacebook',
                'ImgInstagram',
            ]   

            #Renderizamos el html
            html = render_to_string('MAILS/confirmCreateUser.html', {'name': first_name})

            #Enviamos el correo
            email.send_email(
                to      = user.email,
                Cc      = 'jdubaque7@misena.edu.co',
                subject = 'Confirmacion de registro',
                message = html,
                listImage = listImages,
                litsName = listName,
            )
            


            return redirect('login')
        except Exception as e:
            
            print('Error al crear el usuario'+ str(e))
            #Si hay un error el usuario no se crea

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

#--------------------------------- VIEWS API USER ------------------------------------#
def UpdateUser(request):
    if request.method == 'POST':
        try:
            #Recuperamos los datos del formulario
            idUser      = request.POST['idUser']
            username    = request.POST['username']
            email       = request.POST['email']
            first_name  = request.POST['first_name']
            last_name   = request.POST['last_name']
            is_staff    = request.POST['is_staff']
            is_active   = request.POST['is_active']
            
            #Buscamos el usuario
            user = User.objects.get(id=idUser)
            
            #Actualizamos los datos
            user.username   = username
            user.email      = email
            user.first_name = first_name
            user.last_name  = last_name
            user.is_staff   = is_staff
            user.is_active  = is_active
            
            #Guardamos los cambios
            user.save()
            
            return redirect('adminHome')
        except Exception as e:
            print('Error al actualizar el usuario: '+ str(e))
            return redirect('adminHome')
    else:
        return redirect('adminHome')
