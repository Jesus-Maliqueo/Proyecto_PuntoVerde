from django import forms
from .models import LlenadoContenedores,IngresoMaterial




class conteform(forms.ModelForm):
    class Meta:
        model = LlenadoContenedores
        fields = '__all__'

class ingreform(forms.ModelForm):
    class Meta:
        model = LlenadoContenedores
        fields = '__all__'