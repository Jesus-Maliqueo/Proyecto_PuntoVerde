from datetime import date
import datetime
import re
from MySQLdb import Date
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



def registro(request):
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


# -----------------------Contenedor inventario---------------------------

def contnue(request):
 
   if request.method == 'POST':
      id_material = request.POST["ID"]
   
      pesos_material = request.POST['peso']
      tipo_producto = request.POST['material']
      regis= IngresoMaterial.objects.create(id_material=id_material,pesos_material=pesos_material,tipo_producto=tipo_producto)
      regis.save()


   return render(request, 'app/contnue.html')

   # -------------------------------------------
def registerInv(request):
 
   if request.method == 'POST':
      id_contenedo = request.POST["id_contenedor"]
      tipo_contenedor = request.POST['tipo_contenedor']
      pesos = request.POST['peso']
      id_llenado = request.POST['id_llenado']
      regis= InventarioContenedores.objects.create(id_contenedor=id_contenedo,tipo_contenedor=tipo_contenedor,peso=pesos,id_llenado=id_llenado)
      regis.save()


   return render(request, 'app/registrocont.html')



def estado(request):
   # ---Trae informacion de models.py Contenedor

   contenedor = LlenadoContenedores.objects.all()
 
   return render(request, 'app/estado.html', {'contenedor': contenedor  })




def recicla(request):

   return render(request, 'app/recicla.html')







def ingreso(request):
   # ---Trae informacion de models.py  IngresoMaterial
    ingresos = IngresoMaterial.objects.all()
    
    return render(request,'app/prueba.html', {'ingresos':ingresos} )




def mostrar(request): 
  # ---Trae informacion de models.py  Contenedor
    conta= InventarioContenedores.objects.all()
    contenedor = LlenadoContenedores.objects.all()
    ingresos = IngresoMaterial.objects.all()
    
    return render(request,'app/ingreso.html',{'contenedor': contenedor, 'ingresos':ingresos, 'conta':conta} )


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


#--------------creacion contenedores llenando-----------------------
def llenado(request,idi,tipo,pes):
   inv=InventarioContenedores.objects.get(id_contenedor=idi)
   fk=InventarioContenedores.id_contenedor
   incremento=int(idi)+1
   llenar=LlenadoContenedores.objects.create(id_llenado=incremento,tipo_contenedor=tipo,peso=0,estado_contenedor='llenando',precio=pes,invt_conts_id_contenedor=inv)
   
   return redirect('/mostrar/#tab2')
#---------------------------------------------------



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



""" aumento = 0
def asigParteDos(request,id, pesom,pesoc,fk):
   global aumento
   print(pesom)
   print(pesoc)
   aumento = pesom + pesoc
   contenedor = LlenadoContenedores.objects.filter(id_llenado=id)
   if LlenadoContenedores.invt_conts_id_contenedor == InventarioContenedores.id_contenedor:
      if LlenadoContenedores.peso <= InventarioContenedores.peso:
         contenedor = LlenadoContenedores.objects.filter(id_llenado=id).update(peso=aumento)
         aumento+=1
      else: """
         
#--------------------------------------------
