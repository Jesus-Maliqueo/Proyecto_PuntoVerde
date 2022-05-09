from django import forms
from .models import IngresoMaterial


class Conchetumare(forms.ModelForm):

    class Meta:
        model = IngresoMaterial
        fields = "__all__"
        # fields = ["id_material","tipo_producto","fecha","peso_material"]
