#Modelos
from .models import *
from django.contrib.auth.models import User
#Http 
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
#Render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt #importamos excepcion para inhabilitar el csrf

#Views
from django.views.generic import *
#Paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Envio de correos
from django.core.mail import send_mail

#Manejo de excepciones
from django.shortcuts import get_object_or_404

#Tiwilo
from twilio.rest import Client
from .PYtwilo import *

#Envio de correos

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Settings
from django.conf import settings

def home(request):
    
    productos = Product.objects.all()

    return render(request, 'products/homeProducts.html', {'productos': productos})


#--------------------------------- VIEWS PRODUCTS ------------------------------------#

class HomeListView(TemplateView):
    
    template_name = 'products/homeProducts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_products = Product.objects.all()

        # Filtros
        category_filter = self.request.GET.get('category', None)
        color_filter = self.request.GET.get('color', None)
        size_filter = self.request.GET.get('size', None)

        if category_filter:
            all_products = all_products.filter(category=category_filter)
        if color_filter:
            all_products = all_products.filter(color=color_filter)
        if size_filter:
            all_products = all_products.filter(size=size_filter)


        # Paginación
        paginator = Paginator(all_products, 6)  # 4 productos por página
        page = self.request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        
        context["productos"] = products
        context["categorias"] = Categories.objects.all()

        return context
#--------------END-----------------#

class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/DetailProductView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categories.objects.all()
        return context
#--------------END-----------------#



#--------------------------------- VIEWS API CART  ------------------------------------#

def CartList(request):

    if request.method == 'GET':

        session_user = request.session.get('user', None)

        if not Cart.objects.filter(user=session_user).exists():
                return redirect('login')
        else:   
                # Si existe una sesión activa, obtenemos el carrito
                cart = Cart.objects.get(user=request.user)
                # Obtenemos los items del carrito
                items = CartItem.objects.filter(cart=cart)
                # Obtenemos el total de items
                total_items = items.count()
                # Obtenemos el total de la compra}
                total = 0
                
                
                # Calcula el subtotal para cada item y agrega el resultado al contexto
                for item in items:
                    item.subtotal = item.product.price * item.quantity

                # Calcula el total general
                total = sum(item.subtotal for item in items)

                context = {
                    'cart': cart,
                    'items': items,
                    'total_items':total_items,
                    
                    'total': total
                    }

                return  render(request, 'components/carrito.html',context)
#--------------END-----------------#


def addCart(request, id):
    if request.method == 'GET':
        # Obtenemos el usuario de la sesión
        session_user = request.session.get('user', None)
        # Si no existe una sesión activa, redirigimos al login
        if not session_user:
            return redirect('login')
        else:
            # Si existe una sesión activa, obtenemos el carrito
            cart = Cart.objects.get(user=session_user)
            # Obtenemos el producto
            product = Product.objects.get(pk=id)
            # Obtenemos el item del carrito
            item = CartItem.objects.filter(cart=cart, product=product).first()
            # Si el item existe, aumentamos la cantidad
            if item:
                item.quantity += 1
                item.save()
            # Si no existe, lo creamos
            else:
                item = CartItem(
                    cart=cart,
                    product=product
                )
                item.save()
            # Redirigimos al carrito
            return redirect('cart')
    
#--------------END-----------------#


def addOneItemCart(request, id):
    if request.method == 'GET':
        # Obtenemos el usuario de la sesión
        session_user = request.session.get('user', None)
        # Si no existe una sesión activa, redirigimos al login
        if not session_user:
            return redirect('login')
        else:
            # Si existe una sesión activa, obtenemos el carrito
            cart = Cart.objects.get(user=session_user)
            # Obtenemos el producto
            product = Product.objects.get(pk=id)
            # Obtenemos el item del carrito
            item = CartItem.objects.filter(cart=cart, product=product).first()
            # Si el item existe, aumentamos la cantidad
            if item:
                item.quantity += 1
                item.save()
            # Si no existe, lo creamos
            else:
                item = CartItem(
                    cart=cart,
                    product=product
                )
                item.save()
            # Redirigimos al carrito
            return redirect('cart')
#--------------END-----------------#

def removeCart(request, id):
    if request.method == 'GET':
        # Obtenemos el usuario de la sesión
        session_user = request.session.get('user', None)
        # Si no existe una sesión activa, redirigimos al login
        if not session_user:
            return redirect('login')
        else:
            # Si existe una sesión activa, obtenemos el carrito
            cart = Cart.objects.get(user=session_user)
            # Obtenemos el producto
            product = Product.objects.get(pk=id)
            # Obtenemos el item del carrito
            item = CartItem.objects.filter(cart=cart, product=product).first()
            # Si el item existe, aumentamos la cantidad
            if item:
                item.quantity -= 1
                item.save()
                if item.quantity == 0:
                    item.delete()
                    
            # Redirigimos al carrito
            return redirect('cart')
#--------------END-----------------#

def addInCart(request, id):
    if request.method == 'GET':

        
        cantidad = request.GET.get('cantidad', 1) #Recuperamos los datos enviados por el metodo GET

        session_user = request.session.get('user', None) # Obtenemos el usuario de la sesión

        # Si no existe una sesión activa, redirigimos al login
        if not session_user:
            return redirect('login')
        else:
            
            cart = Cart.objects.get(user=session_user) # Si existe una sesión activa, obtenemos el carrito
            
            product = Product.objects.get(pk=id)
            
            item = CartItem.objects.filter(cart=cart, product=product).first()
            
            if item:
                item.quantity = cantidad
                item.save()
            # Si no existe, lo creamos
            else:
                item = CartItem(
                    cart=cart,
                    product=product,
                    quantity=cantidad
                )
                item.save()
            #retornamos una respuesta en formato json
            return JsonResponse({'ok': True})

#--------------------------------- VIEWS API CARTEGORIES ------------------------------------#
def getCategories(request):
    if request.method == 'GET':
        categories = list(Categories.objects.values())

        data = {
            'categories': categories
        }

        return JsonResponse(data)
#--------------END-----------------#


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
#--------------END-----------------#



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
#--------------END-----------------#


def deleteCategories(request, id):

    if request.method == 'DELETE':
        try:
            categoria = Categories.objects.get(pk=id)
            categoria.delete()
            return JsonResponse({'ok': True})
        except Exception as e:
            return JsonResponse({'ok': False, 'error': 'El proceso de eliminación falló'}, status=400)

    return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)
#--------------END-----------------#

#--------------------------------- VIEWS API PRODUCTS ------------------------------------#

def getProducts(request):
    if request.method == 'GET':
        
        # products = list(Product.objects.values('id', 'Product', 'category__', 'description', 'price', 'image'))
        #Consultamos los productos y el nombre de la categoria a la que pertenece
        products = list(Product.objects.values('id', 'Product', 'category__name_categories', 'description', 'price', 'image'))
        data = {
            'products': products
        }

        return JsonResponse(data)
#--------------END-----------------#

def createProducts(request):
        if request.method == 'POST':
            nombre_producto = request.POST.get('nombre_producto')
            categoria_producto = request.POST.get('categoria_producto')
            descripcion_producto = request.POST.get('descripcion')
            precio_producto = request.POST.get('precio')
            imagen_producto = request.FILES.get('imagen')  # Usa request.FILES para obtener el archivo
    
            if nombre_producto and categoria_producto and descripcion_producto and precio_producto and imagen_producto:
                try:
                    producto = Product(
                        Product=nombre_producto,
                        category_id=categoria_producto,
                        description=descripcion_producto,
                        price=precio_producto,
                        image=imagen_producto
                    )
                    producto.save()
                except Exception as e:
                    return JsonResponse({'ok': False, 'error': 'El producto ya existe'}, status=400)
    
                return JsonResponse({'ok': True})
            else:
                return JsonResponse({'ok': False, 'error': 'El proceso de creación falló'}, status=400)
    
        return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)
#--------------END-----------------#


def deleteProducts(request, id):
    
        if request.method == 'DELETE':
            try:
                producto = Product.objects.get(pk=id)
                producto.delete()
                return JsonResponse({'ok': True})
            except Exception as e:
                return JsonResponse({'ok': False, 'error': 'El proceso de eliminación falló'}, status=400)
    
        return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)
#--------------END-----------------#


def updateProducts(request, id):
        
            producto = Product.objects.get(pk=id)
        
            if request.method == 'POST':
                nuevo_nombre = request.POST.get('nombre_producto')
                nueva_categoria = request.POST.get('categoria_producto')
                nueva_descripcion = request.POST.get('descripcion')
                nuevo_precio = request.POST.get('precio')
                nueva_imagen = request.FILES.get('imagen')  # Usa request.FILES para obtener el archivo
        
                if nuevo_nombre and nueva_categoria and nueva_descripcion and nuevo_precio and nueva_imagen:
                    producto.Product = nuevo_nombre
                    producto.category_id = nueva_categoria
                    producto.description = nueva_descripcion
                    producto.price = nuevo_precio
                    producto.image = nueva_imagen
        
                    producto.save()
        
                    return JsonResponse({'ok': True})
                else:
                    return JsonResponse({'ok': False, 'error': 'El proceso de actualización falló'}, status=400)
        
            return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)
#--------------END-----------------#


#--------------------------------- VIEWS SEND MESSAGES ------------------------------------#

#Envio de mensajes
def enviar_mensaje_view(request):
    # Llama a la función para enviar un mensaje
    numero_destino = '+573232093634'
    mensaje = 'Hola esto es una prueba de envio de mensajes desde Django'
    
    # Maneja cualquier error que pueda ocurrir durante el envío
    try:
        mensaje_id = enviar_mensaje_whatsapp(numero_destino, mensaje)
        return HttpResponse(f'Mensaje enviado con ID: {mensaje_id}')
    except Exception as e:
        return HttpResponse(f'Error al enviar el mensaje: {str(e)}', status=500)
#--------------END-----------------#


def sendEmail(request,id):
    # Llama a la función para enviar un mensaje
    usuario = User.objects.get(pk=id)
    asunto = 'Prueba de envío de correo'
    mensaje = render_to_string('components/send_mail.html', {'usuario': usuario})
    remitente = 'designsxilena@gmail.com'
    destinatarios = [
        usuario.email,
        'sanditique071@gmail.com'
    ]
    
    # Maneja cualquier error que pueda ocurrir durante el envío
    try:
        # Enviar el correo electrónico compuesto por un archivo HTML
        send_mail(
            asunto,
            '',
            remitente,
            destinatarios,
            html_message=mensaje
        )
        return HttpResponse('Email enviado correctamente')
    except Exception as e:
        return HttpResponse(f'Error al enviar el mensaje: {str(e)}', status=500)
#--------------END-----------------#





def send_email(request, id):
    try:

        usuario = User.objects.get(pk=id)

        # Si existe una sesión activa, obtenemos el carrito
        cart = Cart.objects.get(user=request.user)
        # Obtenemos los items del carrito
        items = CartItem.objects.filter(cart=cart)
        # Obtenemos el total de items
        total_items = items.count()
        # Obtenemos el total de la compra}
        total = 0
        
        
        # Calcula el subtotal para cada item y agrega el resultado al contexto
        for item in items:
            item.subtotal = item.product.price * item.quantity

        # Calcula el total general
        total = sum(item.subtotal for item in items)


        
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        
        mailServer.starttls()
        
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        

        email_to = usuario.email
        #copiamos correo
        email_cc = [
            'ubaquejuancho@gmail.com'
        ]

        
        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Cc'] = 'ubaquejuancho@gmail.com'
        mensaje['Subject'] = "Compra Confirmada"

        content = render_to_string('components/mail.html', {
            'usuario': usuario,
            'cart': cart,
            'items': items,
            'total_items':total_items,
            'total': total,
            })
        mensaje.attach(MIMEText(content, 'html'))
    
        # Adjuntar imágenes al mensaje con CID
        imgLogo = ConvertImageCid('static/img/LogoXilena.jpg', 'LogoXilena')
        mensaje.attach(imgLogo)
        # Convertimos las demas imagenes 
        BannerNavidad = ConvertImageCid('static/img/images_mail/img_header-airplane.png', 'BannerNavidad')
        mensaje.attach(BannerNavidad)

        ImgFacebook = ConvertImageCid('static/img/images_mail/facebook2x.png', 'ImgFacebook')
        mensaje.attach(ImgFacebook)

        ImgInstagram = ConvertImageCid('static/img/images_mail/instagram2x.png', 'ImgInstagram')
        mensaje.attach(ImgInstagram)


        mailServer.sendmail(settings.EMAIL_HOST_USER,
                            email_to,
                            mensaje.as_string())

        
        

        return redirect('home')
    except Exception as e:
    
        return redirect('home')
#--------------END-----------------#




def test (request):
    usuario = User.objects.get(pk=3)

    # Si existe una sesión activa, obtenemos el carrito
    cart = Cart.objects.get(user=usuario.id)
    # Obtenemos los items del carrito
    items = CartItem.objects.filter(cart=cart)
    # Obtenemos el total de items
    total_items = items.count()
    # Obtenemos el total de la compra}
    total = 0
    
        
    # Calcula el subtotal para cada item y agrega el resultado al contexto
    for item in items:
        item.subtotal = item.product.price * item.quantity

    # Calcula el total general
    total = sum(item.subtotal for item in items)


    context = {
            'usuario': usuario,
            'cart': cart,
            'items': items,
            'total_items':total_items,
            'total': total,
            }
    return render(request, 'MAILS/confirmCreateUser.html', context)