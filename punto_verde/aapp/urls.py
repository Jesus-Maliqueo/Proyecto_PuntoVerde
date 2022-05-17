from django.conf import settings
from django.urls import path
from . import views
from.views import  *
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('registro',views.registro, name="registro"),
    path('recicla', recicla, name="recicla"),
    path('llenado', llenado, name="llenado"),
    path('mostrar',views.mostrar, name='moestrar'),
    path('estado',views.estado, name='estado'),
    path('ingreso',views.ingreso , name='ingreso'),
    path('contreg',views.contreg , name='contreg'),
    path('contnue',views.contnue , name='contnue'),
    path('eliminar/<id>',views.eliminar , name='eliminar'),
    path('eliminar2/<id>',views.eliminar2 , name='eliminar2'),
    path('eliminar3/<id>',views.eliminar3 , name='eliminar3'),
    path('asigParteUno/<id>/<int:peso>',asigParteUno,name="asigParteUno"),
    path('asigParteDos/<id>/<int:pesom>/<int:pesoc>',asigParteDos, name="asigParteDos"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

