from django import forms
from django.forms.forms import Form
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db import connection
from .models import LlenadoContenedores , IngresoMaterial
from .forms import ingreform,conteform

# Create your views here.


def home(request):
   return render(request, 'app/home.html')


def registro(request):
   return render(request, 'app/registro.html')

def estado(request):
   # ---Trae informacion de models.py Contenedor
   contenedor = LlenadoContenedores.objects.all()
 
   return render(request, 'app/estado.html', {'contenedor': contenedor  })

def recicla(request):
   return render(request, 'app/recicla.html')

def llenado(request):
   return render(request, 'app/llenado.html')



def ingreso(request):
   # ---Trae informacion de models.py  IngresoMaterial
    ingresos = IngresoMaterial.objects.all()
    return render(request,'app/prueba.html', {'ingresos':ingresos} )


def mostrar(request): 
  # ---Trae informacion de models.py  Contenedor
    contenedor = LlenadoContenedores.objects.all()
    return render(request,'app/ingreso.html',{'contenedor': contenedor })



