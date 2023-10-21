from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.views.generic import *

# Create your views here.
@login_required
def adminHome(request):
    return render(request, 'adminHome.html')


def LoginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate (username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('adminHome')  # Redirigir al adminHome

        else:
            return redirect('products:homeProducts')
    return render(request, 'registration/login.html')



def logout(request):
    return redirect('products:homeProducts')