from django import forms


class VenderFormulario(forms.Form):

    
    marca = forms.CharField(max_length=40) 
    modelo = forms.CharField(max_length=40)
    anio = forms.IntegerField()

