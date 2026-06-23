from django import forms
from .models import Parroquia, Barrio

class ParroquiaForm(forms.ModelForm):
    class Meta:
        model = Parroquia
        fields = '__all__'


class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = '__all__'