from unicodedata import name
from django.conf import settings
from django.urls import path, include
from . import views
from.views import  *
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('registro/',registro, name="registro"),
    path('empresa/',empresa, name="empresa"),
    path('recicla/', recicla, name="recicla"),
    path('retiro/<id>',retiro, name="retiro"),
    path('mostrar/',views.mostrar, name='mostrar'),
    path('estado/',views.estado, name='estado'),
    path('ingreso/',views.ingreso , name='ingreso'),
    path('contnue',views.contnue , name='contnue'),
    path('eliminar/<id>',views.eliminar , name='eliminar'),
    path('eliminar2/<id>',views.eliminar2 , name='eliminar2'),
    path('eliminar3/<id>',views.eliminar3 , name='eliminar3'),
    path('asigParteUno<id>/<int:peso>',asigParteUno,name="asigParteUno"),
    path('asigParteDos<id>/<int:pesom>/<int:pesoc>',asigParteDos, name="asigParteDos"),
    path('registerInv',registerInv,name="registerInv"),
    path('llenado<idi>/<tipo>/<pes>',llenado,name="llenado"),
    path('lleno/<ida>/<tipo>/<peso>' ,lleno,name="lleno"),
    path('comprador',views.comprador, name='comprador'),
    path('lleno1/',lleno1,name="lleno1"),
    path ('accounts/',include('django.contrib.auth.urls')),
    path('reservar/<id>/<us>',reservar,name="reservar"),
    path('emple/', emple,name="emple"),
    path('eliEmple/<id>',eliEmple,name="eliEmple"),
    path('horpart1/<id>',horpart1, name="horpart1"),
    path('horpart2/<id>',horpart2, name="horpart2"),
    path('compra/<a>',compra, name="compra"),
    path('enviar/',post, name='enviar'),
    path('adm/',admin,name="adm"),
    path('tables/',tables,name="tables"),
    path('mishorarios/<id>',mishorarios,name="mishorarios"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

