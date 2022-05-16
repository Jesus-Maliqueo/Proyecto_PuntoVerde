import re
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
from .models import LlenadoContenedores , IngresoMaterial,InventarioContenedores
from .forms import Conchetumare,Conchetumare2,Conchetumare3

# Create your views here.


def home(request):
   return render(request, 'app/home.html')



def registro(request):

   data={
      'form': Conchetumare3()
   }

   if request.method =='POST':
      formulario = Conchetumare3(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "se guardo con exito"

      else:
         data['form'] = formulario

   return render(request, 'app/registro.html',data)


# ---------------------------------------------
def contreg(request):
   data={
      'form': Conchetumare2()
   }


   if request.method =='POST':
      formulario = Conchetumare2(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "se guardo"
      else:
         data['form'] = formulario

   return render(request, 'app/registrocont.html',data)

# -----------------------Contenedor inventario---------------------------

def contnue(request):
   data={
      'form': Conchetumare(),
   }

   if request.method =='POST':
      formulario = Conchetumare(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "se guardo"

      else:
         data['form'] = formulario

   return render(request, 'app/contnue.html',data)

   # -------------------------------------------




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
    print( IngresoMaterial.id_material("1"))
    return render(request,'app/prueba.html', {'ingresos':ingresos} )




def mostrar(request): 
  # ---Trae informacion de models.py  Contenedor
    contenedor = LlenadoContenedores.objects.all()
    ingresos = IngresoMaterial.objects.all()
    cont= InventarioContenedores.objects.all()
    return render(request,'app/ingreso.html',{'contenedor': contenedor, 'ingresos':ingresos, 'cont':cont} )


# -------------------------------Eliminar Boton----------------------------------------
def eliminar(request, id):
   contenedor = LlenadoContenedores.objects.get(id_llenado=id)
   contenedor.delete()
   return redirect('/mostrar/#tab2')


def eliminar2(request, id):
   contenedor = IngresoMaterial.objects.get(id_material=id)
   contenedor.delete()
   return redirect('/mostrar/#tab3')

def eliminar3(request, id):
   contenedor = InventarioContenedores.objects.get(id_contenedor=id)
   contenedor.delete()
   return redirect('/mostrar/#tab1')

# --------------------------------------------------------------------------------------


llenando = llenandoForm()
def asignacion(request):
   global llenando 
   data={
      'form': llenandoForm()

   }
   if request.method =='POST':
      llenando = llenandoForm(request.POST, request.FILES)
      if llenando.is_valid():
         llenando.save()
         data["mensaje"] = "se guardo"
         return redirect('estado')
      else:
         data['form'] = llenando


   return render(request, 'app/asignar.html',{'llenando':llenando})
