from django import forms
from .models import Contenedor,IngresoMaterial




class conteform(forms.ModelForm):
    class Meta:
        model = Contenedor
        fields = '__all__'

class ingreform(forms.ModelForm):
    class Meta:
        model = Contenedor
        fields = '__all__'