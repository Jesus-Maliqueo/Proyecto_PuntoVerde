from django.contrib import admin
from .models import Horarios, InventarioContenedores,LlenadoContenedores,Boleta,Comprador,ContenedorLleno,Empleado,Factura,Informe,IngresoMaterial, Precios,Reserva,Retiro,Compra,Horarios
# Register your models here.

class ingreso(admin.ModelAdmin):
    list_display = ["id_material","tipo_producto","fecha","pesos_material"]
    list_editable =["pesos_material"]
    list_filter = ["tipo_producto"]

class lcontenedor(admin.ModelAdmin):
    list_display = ["id_llenado","tipo_contenedor","peso","estado_contenedor","precio"]
    list_editable =["peso","precio"]
    list_filter = ["tipo_contenedor"]

class ncontenedor(admin.ModelAdmin):
    list_display = ["id_contenedor","tipo_contenedor","peso","id_llenado"]
    list_editable =["tipo_contenedor","peso"]
    list_filter = ["tipo_contenedor"]

class precio(admin.ModelAdmin):
    list_display = ["id_precio","tipo_material","descripcion","precio"]
    list_filter = ["tipo_material"]

class bole(admin.ModelAdmin):
    list_display = ["id_venta","nombre","forma_pago"]
    list_filter = ["forma_pago"]

class comp(admin.ModelAdmin):
    list_display = ["id_venta","monto","forma_pago","fecha_venta","emitido_en"]
    list_filter = ["forma_pago"]

class compr(admin.ModelAdmin):
    list_display = ["id_comprador","nombre","direccion","telefono","correo"]
    list_filter = ["nombre"]

class contll(admin.ModelAdmin):
    list_display = ["id_lleno","reservado","lleno","precios_id_precio"]
    list_filter = ["id_lleno","reservado"]

class emple(admin.ModelAdmin):
    list_display = ["rut_empleado","primer_nombre","segundo_nombre","primer_apellido","segundo_apellido","direccion","telefono","ocupacion"]
    list_filter = ["primer_apellido","ocupacion"]

class fac(admin.ModelAdmin):
    list_display = ["id_venta","nombre_empresa","giro_industria","region","comuna"]
    list_filter = ["nombre_empresa","region","comuna"]

class info(admin.ModelAdmin):
    list_display = ["id_infome","fecha_informe"]
    list_filter = ["fecha_informe"]


class reser(admin.ModelAdmin):
    list_display = ["id_reserva","fecha","fecha_limite"]
    list_filter = ["fecha"]

class ret(admin.ModelAdmin):
    list_display = ["id_retiro","primer_nombre","segundo_nombre","primer_apellido","segundo_apellido","fecha_retiro","contacto"]
    list_filter = ["primer_apellido","fecha_retiro"]

class hor(admin.ModelAdmin):
    list_display = ["id_horario","hora_inicio","hora_termino"]
    list_filter = ["hora_inicio","hora_termino"]

admin.site.register(Horarios,hor)
admin.site.register(Precios,precio)
admin.site.register(Boleta,bole)
admin.site.register(Comprador,compr)
admin.site.register(LlenadoContenedores,lcontenedor)
admin.site.register(ContenedorLleno,contll)
admin.site.register(InventarioContenedores,ncontenedor)
admin.site.register(Empleado,emple)
admin.site.register(Factura,fac)
admin.site.register(Informe,info)
admin.site.register(IngresoMaterial,ingreso)
admin.site.register(Reserva,reser)
admin.site.register(Retiro,ret)
admin.site.register(Compra,comp) 

