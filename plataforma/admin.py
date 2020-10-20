from django.contrib import admin
from .models import *

# Register your models here.

class AreaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'descripcion', 'ocultar')
	list_filter = ['id']
	search_fields = ['nombre']

admin.site.register(Area, AreaAdmin)

class NivelAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'descripcion', 'ocultar')
	list_filter = ['id']
	search_fields = ['nombre']

admin.site.register(Nivel, NivelAdmin)

class PlataformaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'objetivo', 'enlace', 'fotografia', 'fecha_de_creacion','observaciones_sugerencias','ocultar')
	list_filter = ['id']
	search_fields = ['enlace']

admin.site.register(Plataforma, PlataformaAdmin)
