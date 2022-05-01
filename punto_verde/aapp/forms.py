""" from faulthandler import disable
from django import forms
from django.forms import ModelForm,widgets 
from .models import IngresoMaterial

class IngresarForm(ModelForm):

    class Meta:
        model = IngresoMaterial
        fields = ['id_material','tipo_producto','fecha','pesos_material','receptor_rut_receptor','contenedor_id_contenedor']

        labels={
            'id_material':"id_Material:",
            'tipo_producto': "Tipo:",
            'fecha' : "Fecha:",
            'pesos_material': "Peso:",
            'receptor_rut_receptor': "Receptor",
            'contenedor_id_contenedor' : "Contenedor:"
        }

        widgets={
            'id_material':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'material', 
                    'name': 'material',
                    'placeholder': 'ingreso_material',
                    'disabled':'disabled'
                }
            ),
            
            'tipo_producto':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'producto', 
                    'name': 'producto',
                    'placeholder': 'tipo',
                    'disabled':'disabled'
                }
            ),
            'fecha':forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fecha', 
                    'name': 'fecha',
                    'placeholder': 'fecha',
                    'disabled':'disabled'
                }
            ),
            'pesos_material':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'peso', 
                    'name': 'peso',
                    'placeholder': 'peso',
                    'disabled':'disabled'
                }
            ),
            'receptor_rut_receptor':forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'rut', 
                    'name': 'rut',
                    'placeholder': 'rut'
                }
            ),
            'contenedor_id_contenedor':forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'contenedor', 
                    'name': 'contenedor',
                    'placeholder': 'contenedor'
                    'required'
                }
            ),
            
        }
 """