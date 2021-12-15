from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Vender



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

        venderalgo = Vender(marca=request.POST["marca"] , modelo=request.POST["modelo"], anio=request.POST["anio"]) #VA EN MAYUSCULA LPM
        

        venderalgo.save()

        return render(request, 'AppCoder/inicio.html')


    return render(request, 'AppCoder/vender.html')


