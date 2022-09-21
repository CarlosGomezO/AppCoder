from django.db import models

# Create your models here.

class familia(models.Model):
    
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()


class entregable(models.Model):
    
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fecha = models.DateField()
    
    
class personas(models.Model):
    
    dni = models.IntegerField()
    nombre = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    
class empleos(models.Model):
    
    nombre = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60)
    rubro = models.CharField(max_length=60)

class informacion(models.Model):
    
    dni = models.IntegerField()
    instagram = models.IntegerField()
    email = models.EmailField()
    
    
    