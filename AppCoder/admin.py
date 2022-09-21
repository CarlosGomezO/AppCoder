from django.contrib import admin

# Register your models here.

from AppCoder.models import *


admin.site.register(personas)
admin.site.register(empleos)
admin.site.register(informacion)

