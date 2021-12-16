from django.urls import path
from AppCoder import views



urlpatterns = [
 

    path('inicio', views.inicio, name="Inicio"),
    path('vehiculos', views.vehiculos, name="Vehiculos"),
    path('inmaculados', views.inmaculados , name="Inmaculados" ),
    path('ofertas', views.ofertas , name="Ofertas"),
    path('vender', views.vender , name="Vender"),
    path('busquedaAuto', views.busquedaAuto ),
   
]