from django.shortcuts import render
from django.http import HttpResponse


from AppCoder.models import Vender

from AppCoder.forms import VenderFormulario




# Create your views here.


def inicio(request):

    # return HttpResponse("Inicio del proyecto")
    return render(request, 'AppCoder/inicio.html')


def vehiculos(request):
    
    return render(request, 'AppCoder/vehiculos.html')


def inmaculados(request):

    return render(request, 'AppCoder/inmaculados.html')

def ofertas(request):

    return render(request, 'AppCoder/ofertas.html')
    
def vender(request):

    if request.method == "POST":

        VFormulario = VenderFormulario(request.POST)

        if VFormulario.is_valid():

            informacion =VFormulario.cleaned_data

            venderalgo = Vender(marca=informacion["marca"] , modelo=informacion["modelo"], anio=informacion["anio"]) #VA EN MAYUSCULA LPM
        

            venderalgo.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        VFormulario = VenderFormulario()

       


    return render(request, 'AppCoder/vender.html' , {"VFormulario" : VFormulario})

def busquedaAuto(request):

    return render(request, 'AppCoder/busquedaAuto.html')


