from django.contrib import admin
from .models import *

# Register your models here.

class EnlaceAdmin(admin.ModelAdmin):
	list_display = ['id', 'enlace', 'descripcion']
	list_filter = ['descripcion']
	search_fields = ['enlace']

admin.site.register(Enlace, EnlaceAdmin)

class HerramientaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'enlace', 'fecha_de_creacion', 'ocultar')
	list_filter = ['id']
	search_fields = ['enlace']

admin.site.register(Herramienta, HerramientaAdmin)
