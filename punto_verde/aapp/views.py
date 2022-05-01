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
import cx_Oracle
# Create your views here.


def home(request):
   return render(request, 'app/home.html')


def registro(request):
   return render(request, 'app/registro.html')

def estado(request):
   return render(request, 'app/estado.html')

def recicla(request):
   return render(request, 'app/recicla.html')

def llenado(request):
   return render(request, 'app/llenado.html')

def mostrar(request):
    return render(request,'app/ingreso.html')

""" def asignacion(request,id):
   forma = IngresoMaterial.objects.get(id_material=id)
   datos ={
      'form': IngresarForm(instance=forma)
   }
   if request.method == 'POST':
      asignara = IngresarForm(data=request.POST, instance=forma)
      if asignara.is_valid():
            asignara.save()
            return redirect('mostrar')
   return render(request, 'app/asignar.html',datos)
 """






""" def agregar_contenedor(p_ID_CONTENEDOR, p_TIPO_material, p_PESO, v_salida):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.number)
    cursor.callproc('sp_agregar_cont',[p_ID_CONTENEDOR, p_TIPO_material, p_PESO, v_salida]) 
    return salida.getvalue() """


""" def registro2(request):
   registro=IngresoMaterial.objects.all()

    #agregar_usuario
   if request.method == 'POST':
      
      id_contenedor = request.POST.get('rut')
      tipo_material = request.POST.get('producto')
      peso = request.POST.get('peso')
   
      salida = agregar_contenedor(id_contenedor, tipo_material, peso)
      if salida == 1:
            print ('se ha agregado el material al contenedor')
      else:
            print ('no se ha podido guardar')

   return render(request, 'app/registration/registro2.html')
 """