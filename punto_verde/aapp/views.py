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
from .models import LlenadoContenedores , IngresoMaterial,InventarioContenedores,Empleado
from .forms import Conchetumare,Conchetumare2,Conchetumare3

# Create your views here.


def home(request):
   return render(request, 'app/home.html')



def registro(request ,*callback_args, **callback_kwargs):
   if request.method == 'POST':
      rut_empleado = request.POST["rut"]
      primer_nombre = request.POST['primer_nombre']
      segundo_nombre = request.POST['segundo_nombre']
      primer_apellido = request.POST['primer_apellido']
      segundo_apellido = request.POST['segundo_apellido']
      direccion = request.POST['direccion']
      telefono = request.POST['telefono']
      ocupacion = request.POST['ocupacion']
      regis= Empleado.objects.create(rut_empleado=rut_empleado,primer_nombre=primer_nombre,segundo_nombre=segundo_nombre,primer_apellido=primer_apellido,segundo_apellido=segundo_apellido,direccion=direccion,telefono=telefono,ocupacion=ocupacion)
      regis.save()




   return render(request,'app/registro.html')


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
   return redirect('/mostrar#tab2/')


def eliminar2(request, id):
   contenedor = IngresoMaterial.objects.get(id_material=id)
   contenedor.delete()
   return redirect('/mostrar/#tab3')

def eliminar3(request, id):
   contenedor = InventarioContenedores.objects.get(id_contenedor=id)
   contenedor.delete()
   return redirect('/mostrar/#tab1')

# --------------------------------------------------------------------------------------







#---------------asignando-------------
def asigParteUno(request,id,peso):
   material= IngresoMaterial.objects.get(id_material=id)
   contenedor = LlenadoContenedores.objects.all()
   print(LlenadoContenedores.peso)
   peso_material = peso
   aumento = peso_material
   return render(request,'app/asignar.html',{'contenedor':contenedor,'pesoM' : peso_material})


aumento = 0
def asigParteDos(request,id, pesom,pesoc):
   global aumento
   print(pesom)
   print(pesoc)
   aumento = pesom + pesoc
   contenedor = LlenadoContenedores.objects.filter(id_llenado=id).update(peso=aumento)
   return redirect('/mostrar/#tab2')
#--------------------------------------------