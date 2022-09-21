import email
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

# Create your views here.





# HTML

def inicio(request): #inicio.html  - muestra todo
    
    return render(request, "AppCoder/inicio.html")


def control(request): #control.html - muestra todo
    
    return render(request, "AppCoder/control.html")






# FORMULARIO ------------------------------------------


def formulario1(request):
    
    if request.method=="POST":
    
        personasF = personas(nombre=request.POST["nombre"], dni=request.POST["dni"], fecha_nacimiento=request.POST["fecha"] )
    
        personasF.save()
    
        return render(request, "AppCoder/formu1.html")
    
    return render(request, "AppCoder/formu1.html")


def formulario2(request):
    
    if request.method=="POST":
    
        EmpleosF = empleos(nombre=request.POST["nombre"], empresa=request.POST["empresa"], rubro=request.POST["rubro"] )
    
        EmpleosF.save()
    
        return render(request, "AppCoder/formu2.html")
    
    return render(request, "AppCoder/formu2.html")



def formulario3(request):
    
    if request.method=="POST":
    
        InformacionF = informacion(dni=request.POST["dni"], instagram=request.POST["instagram"], email=request.POST["email"] )
    
        InformacionF.save()
    
        return render(request, "AppCoder/formu3.html")
    
    return render(request, "AppCoder/formu3.html")






# Busqueda Database ------------------------------------------

def busquedaDB(request):
    
    return render(request, "AppCoder/busqueda.html")


def muestraDB(request):
    
    
    busqueda = request.GET["dni"]
    
    return HttpResponse(f"Estoy buscando en Database: {busqueda}")














# -------------------------------------------------------

def familiares(request):
    
    famy = familia(nombre = "Jessica", apellido="gomez", edad = 26 )
    
    famy.save()
    texto = f"Famy: nombre: {famy.nombre}" 
    return HTTPResponse(texto)


def integrantes(request):
    
    Ellos = entregable(nombre = "Carlos", edad = 28, fecha = "1994-4-19" )
    
    Ellos.save()
    
    return HttpResponse(f"He guardado: {Ellos.nombre} con fecha {Ellos.fecha} y edad: {Ellos.edad}") 

