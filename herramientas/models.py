from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator

# Create your models here.
class Enlace(models.Model):
	id = models.AutoField(primary_key = True)
	enlace = models.CharField('Enlace de la Herramienta', 
		max_length = 150)
	descripcion = models.TextField('Descripción', 
		validators=[MaxLengthValidator(1000)])
	ocultar = models.BooleanField('Ocultar Enlace', default=False)
	class Meta:
		verbose_name_plural = 'Enlaces de Herramientas'
		ordering = ['id']
	def __str__(self):
		return self.enlace

class Herramienta(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField('Nombre de la Herramienta', 
		max_length = 150)
	descripcion = models.TextField('Descripción', 
		validators=[MaxLengthValidator(1000)])
	enlace = models.ForeignKey(Enlace, on_delete=models.PROTECT, 
		help_text='Seleccione el Enlace.')
	fotografia = models.ImageField(upload_to = 'herramienta/', 
		default='herramienta/image.jpg',
		help_text='Suba imágenes (jpg, gif, png).')
	fecha_de_creacion = models.DateField(auto_now_add=True)
	observaciones_sugerencias = models.TextField('Describa las observaciones y sugerencias', 
		blank = True, validators=[MaxLengthValidator(1500)])
	ocultar = models.BooleanField('Herramienta descontinuada', default=False)
	class Meta:
		verbose_name_plural = 'Herramientas'
		ordering = ['id']
	def __str__(self):
		return self.nombre