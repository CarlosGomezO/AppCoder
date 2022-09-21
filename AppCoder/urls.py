from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    
    path("Inicio/",inicio, name="beginning"),
    path("Entregable/",integrantes, name= "database"),
    path("control/",control, name="support"),
    path("formu1/", formulario1),
    path("formu2/",formulario2),
    path("formu3/", formulario3),
    path("busquedaDB/", busquedaDB),
    path("buscar/", muestraDB),
    
]