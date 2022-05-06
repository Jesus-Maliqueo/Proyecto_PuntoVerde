from django.contrib import admin
from .models import InventarioContenedores,LlenadoContenedores,Boleta,Comprador,ContenedorLleno,DetaAsignacion,Empleado,Factura,Informe,IngresoMaterial,Receptor,Reserva,Retiro,Venta
# Register your models here.


admin.site.register(Boleta)
admin.site.register(Comprador)
admin.site.register(LlenadoContenedores)
admin.site.register(ContenedorLleno)
admin.site.register(DetaAsignacion)
admin.site.register(InventarioContenedores)
admin.site.register(Empleado)
admin.site.register(Factura)
admin.site.register(Informe)
admin.site.register(IngresoMaterial)
admin.site.register(Receptor)
admin.site.register(Reserva)
admin.site.register(Retiro)
admin.site.register(Venta) 