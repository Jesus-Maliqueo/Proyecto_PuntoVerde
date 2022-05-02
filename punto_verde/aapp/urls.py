from django.urls import path
from . import views
from.views import  estado, home, llenado, recicla, registro, mostrar

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('recicla/', recicla, name="recicla"),
    path('llenado/', llenado, name="llenado"),
    path('mostrar/',views.mostrar,name="mostrar"),
    path('estado/',views.estado, name='estado')

]
