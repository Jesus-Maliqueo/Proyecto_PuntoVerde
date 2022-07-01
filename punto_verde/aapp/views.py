from ast import Return
from datetime import date , timedelta
import datetime
import re
from MySQLdb import Date
from django import forms
from django.forms.forms import Form
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.db import connection
from .models import LlenadoContenedores , IngresoMaterial,InventarioContenedores,Empleado
from django.core.mail import send_mail  
from django.db.models import Count
import stripe
from django.conf import Settings
from django.urls import reverse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# Create your views here.


def home(request):
   return render(request, 'app/home.html')



def registro(request):
   if request.method == 'POST':
      rut = request.POST["rut"]
      primer_nombre = request.POST['primer_nombre']
      segundo_nombre = request.POST['segundo_nombre']
      primer_apellido = request.POST['primer_apellido']
      segundo_apellido = request.POST['segundo_apellido']
      contraseña = request.POST['contraseña']
      email = request.POST['email']
      direccion = request.POST['direccion']
      telefono = request.POST['telefono']
      ocupacion = request.POST['ocupacion']
      regis= Empleado.objects.create(rut_empleado=rut,primer_nombre=primer_nombre,segundo_nombre=segundo_nombre,primer_apellido=primer_apellido,segundo_apellido=segundo_apellido,password=contraseña,email=email,direccion=direccion,telefono=telefono,ocupacion=ocupacion)
      user = authenticate(request, username=primer_nombre, password=segundo_nombre)
      empleado= Empleado.objects.get(rut_empleado=rut)

      if empleado.ocupacion == "Admin":
         user = User.objects.create_user(empleado.rut_empleado, empleado.email)
         user.last_name = empleado.primer_nombre  
         user.is_staff=True
         user.set_password(empleado.password)
         user.groups.add('2')
         # permisos jesus - admin 2
         # permisos mati -  admin 5
         user.save()
      elif empleado.ocupacion == "Empleado":
         user = User.objects.create_user(empleado.rut_empleado, empleado.email)
         user.last_name = empleado.primer_nombre  
         user.is_staff=False
         user.set_password(empleado.password)
         user.groups.add('3')
         # permisos jesus  emplado 3
         # permisos mati  empleado 6 
         user.save()
      else:
         user = User.objects.create_user(empleado.rut_empleado, empleado.email)
         user.last_name = empleado.primer_nombre  
         user.is_staff=False
         user.set_password(direccion)
         user.groups.add('4')
         # permisos jesus receptor 4 
         # permisos mati receptor 7

         user.save()
      return redirect(emple)
   else:
      ...
   
   
   return render(request,'app/registro.html')

# ---------------------------------------------


# -----------------------Ingreso Material---------------------------

def contnue(request):
 
   if request.method == 'POST':
      pesos_material = request.POST['peso']
      tipo_producto = request.POST['material']
      regis= IngresoMaterial.objects.create(pesos_material=pesos_material,tipo_producto=tipo_producto,estado='S')
      regis.save()
      return redirect('/mostrar/#tab3')


   return render(request, 'app/contnue.html')

# -----------------------Contenedor inventario---------------------------
def registerInv(request):
 
   if request.method == 'POST':
      tipo_contenedor = request.POST['tipo_contenedor']
      pesos = request.POST['peso']
      id_llenado = request.POST['id_llenado']
      regis= InventarioContenedores.objects.create(tipo_contenedor=tipo_contenedor,peso=pesos,id_llenado=id_llenado)
      regis.save()
      return redirect('/mostrar/#tab1')

   return render(request, 'app/registrocont.html')


# -----------------------Registro comprador ---------------------------

def comprador(request):
 
   if request.method == 'POST':
      id = request.POST["id_comprador"]
      nombre = request.POST['nombre']
      contra = request.POST['contraseña']
      direccion = request.POST['direccion']
      telefono = request.POST['telefono']
      corr = request.POST['correo']
      regis= Comprador.objects.create(id_comprador=id,nombre=nombre,password=contra,direccion=direccion,telefono=telefono,correo=corr)
      regis.save()
      com=Comprador.objects.get(id_comprador=id)
      user = User.objects.create_user(com.id_comprador, com.correo)
      user.first_name = com.nombre  
      user.is_staff=False
      user.set_password(com.password)
      user.groups.add('1')
      # permisos jesus 1
      # permisos mati 4
      user.save()
      return redirect(home)


   return render(request, 'app/comprador.html')


  
#--------------------------------Formulario RESERVA---------------
cont=0
def reservar(request,id,us):
      usuario=Comprador.objects.get(id_comprador=us)
      fk=ContenedorLleno.objects.get(id_lleno=id)
      cont=int(id)+1
      fechahoy=date.today()
      limite=fechahoy+ timedelta(30)
      print(fechahoy)
      print(limite)
      resev=Reserva.objects.create(id_reserva=cont,fecha=fechahoy,fecha_limite=limite,contenedor_lleno_id_lleno=fk,comprador_id_comprador=usuario)
      aso=ContenedorLleno.objects.filter(id_lleno=id).update(reservado='S',reserva_id_reserva=resev)
      ver=Reserva.objects.get(id_reserva=cont)
      datos ={
      'reserva':ver,
      'usuario':usuario
      }
      return render(request,'app/reserva.html',datos)

# --------------------------REGISTRO RETIRO-----------------------------------------

def retiro(request,id):
   ver=Reserva.objects.get(id_reserva=id)
   
   if request.method == 'POST':
      id_r = request.POST["id_retiro"]
      primer_nombre = request.POST['primer_nombre']
      segundo_nombre = request.POST['segundo_nombre']
      primer_apellido = request.POST['primer_apellido']
      segundo_apellido = request.POST['segundo_apellido']
      fecha_retiro = request.POST['fecha_retiro']
      contacto = request.POST['contacto']
      regis= Retiro.objects.create(id_retiro=id_r,primer_nombre=primer_nombre,segundo_nombre=segundo_nombre,primer_apellido=primer_apellido,segundo_apellido=segundo_apellido,fecha_retiro=fecha_retiro,contacto=contacto)
     
   else:
      ...
   return render(request, 'app/retiro.html',{'vera':ver})
 

# ------------------------------ Registro Compra -------------------------------------
def compra(request,a): #fk
   ver=Reserva.objects.get(id_reserva=a)
   # re=Retiro.objects.get(id_retiro=fk)
   if request.method == 'POST':
      iventa = request.POST["id_venta"]
      monto = request.POST['monto']
      forma_pago = request.POST['forma_pago']
      fecha_venta = request.POST['fecha_venta']
      emitido_en = request.POST['emitido_en']
      regis= Compra.objects.create(id_venta=iventa,monto=monto,forma_pago=forma_pago,fecha_venta=fecha_venta,emitido_en=emitido_en,reserva_id_reserva=ver) #retiro_id_retiro=re
      return redirect(lleno1)

   return render(request, 'app/compra.html')



# -------------------------------------------------------------------




@login_required
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



@login_required
def mostrar(request): 
  # ---Trae informacion de models.py  Contenedor
    conta= InventarioContenedores.objects.all()
    contenedor = LlenadoContenedores.objects.all()
    ingresos = IngresoMaterial.objects.all()
    llenos=ContenedorLleno.objects.all()

    return render(request,'app/ingreso.html',{'contenedor': contenedor, 'ingresos':ingresos, 'conta':conta,'llenos':llenos} )


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




# ------------------Traslado de cont.lleno a venta y vista de CONTENDOR LLENO
@login_required
def lleno1(request):

   llenos=ContenedorLleno.objects.all()

   return render(request,'app/llenado.html',{'llenos':llenos})

@login_required
def lleno(request,ida,tipo,peso):


   a = Precios.objects.filter(tipo_material=tipo)

   print(a)
   lalo = LlenadoContenedores.objects.get(id_llenado=ida)

   if tipo == 'c' or tipo == 'C':

      fk= Precios.objects.get(id_precio=1)
      print(fk)
      suma = int(ida)+1
      p=fk.precio
      print(p)
      print(peso)
      total=p*int(peso)

      llenor = ContenedorLleno.objects.create(id_lleno=suma,reservado='N',precio_total=total,estado='N',llen_conts_id_llenado=lalo,precios_id_precio=fk)


#   ---------- Precio Envace 
   else:
      fk= Precios.objects.get(id_precio=2)
      suma = int(ida)+1

      p=fk.precio
      print(p)
      print(peso)
      total=p*int(peso)
      llenor = ContenedorLleno.objects.create(id_lleno=suma,reservado='N',precio_total=total,estado='N',llen_conts_id_llenado=lalo,precios_id_precio=fk)





   return redirect('/mostrar/#tab4')






#---------------asignando-------------
def asigParteUno(request,id,peso):
   material= IngresoMaterial.objects.get(id_material=id)
   contenedor = LlenadoContenedores.objects.all()
   print(LlenadoContenedores.peso)
   peso_material = peso
   aumento = peso_material
   estadoingreso = IngresoMaterial.objects.filter(id_material=id).update(estado='U')
   return render(request,'app/asignar.html',{'contenedor':contenedor,'pesoM' : peso_material})



aumento = 0
def asigParteDos(request,id, pesom,pesoc):
   global aumento
   print(pesom)
   print(pesoc)
   aumento = pesom + pesoc
   print(aumento)
   contenedor = LlenadoContenedores.objects.filter(id_llenado=id).update(peso=aumento)
   actualizacion = LlenadoContenedores.objects.get(id_llenado=id)
   if actualizacion.peso < actualizacion.precio:
      actualizacion = LlenadoContenedores.objects.filter(id_llenado=id).update(estado_contenedor="lleno")
      messages.info(request, 'el contenedor aun esta llenandose')
      return redirect('/mostrar/#tab2')
   elif actualizacion.peso == actualizacion.precio:
      messages.success(request, 'el contenedor se lleno ')
      return redirect('/mostrar/#tab2')
   elif actualizacion.peso > actualizacion.precio:
      messages.warning(request, 'ya no se puede ingresar mas material al contenedor')
      actualizacion = LlenadoContenedores.objects.filter(id_llenado=id).update(peso=pesoc)
      return redirect('/mostrar/#tab2')
   return redirect('/mostrar/#tab2')


#--------horarios-----------------------------
def horpart1(request,id):
   dato=Empleado.objects.get(rut_empleado=id)
   datos={
      'empleado':dato
   }
   
   return render(request, 'app/horarios.html',datos)

def horpart2(request,id):
   empl=Empleado.objects.get(rut_empleado=id)
   if request.method == 'POST':
      
      inicio = request.POST['inicio']
      termino = request.POST['termino']
      
      crear=Horarios.objects.create(hora_inicio=inicio ,hora_termino=termino,empleado_rut_empleado=empl)
      return redirect(emple)
   else:
      ...
   return render(request, 'app/horarios.html')

#--------horarios-----------------------------
def emple(request):
   lista=Empleado.objects.all()
   return render(request,'app/empleados.html',{'lista':lista})

def eliEmple(request,id):
   us=Empleado.objects.get(rut_empleado=id)
   usuario=User.objects.filter(username=id)
   us.delete()
   usuario.delete()

   return redirect(emple)


    
def post(request):
   usuario = request.POST.get('comprador')
   email = request.POST.get('email')
   telefono = request.POST.get('telefono')
   conte = request.POST.get('contenedor')
   inicio = request.POST.get('inicio')
   fin = request.POST.get('fin')
   print(email)

   template = get_template('app/envio.html')

   # Se renderiza el template y se envias parametros
   content = template.render({'usuario':usuario,'telefono':telefono,'email': email,'conte':conte,'inicio':inicio,'fin':fin})

   # Se crea el correo (titulo, mensaje, emisor, destinatario)
   msg = EmailMultiAlternatives(
         'Gracias por tu reserva',
         'Hola, te enviamos un correo con tu factura',
         settings.EMAIL_HOST_USER,
         [email]
   )

   msg.attach_alternative(content, 'text/html')
   msg.send()

   return render(request, 'app/reserva.html')

def admin(request):
   inventario=InventarioContenedores.objects.all()
   return render(request,'dashboard/index.html',{'invent':inventario})
def tables(request):
   contenedor = LlenadoContenedores.objects.all()
   return render(request,'dashboard/tables.html',{'contenedor': contenedor  })
