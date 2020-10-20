from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator

# Create your models here.

class Area(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField('Nombre del área', 
		max_length = 150)
	Descripcion = models.TextField('Descripción del área', 
		validators=[MaxLengthValidator(1000)])
	ocultar = models.BooleanField('Ocultar área', default=False)
	class Meta:
		verbose_name_plural = 'Áreas'
		ordering = ['id']
	def __str__(self):
		return self.nombre

class Nivel(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField('Nivel Académico', 
		max_length = 150)
	Descripcion = models.TextField('Descripción del Nivel Académico', 
		validators=[MaxLengthValidator(1000)])
	ocultar = models.BooleanField('Ocultar Nivel Académico', default=False)
	class Meta:
		verbose_name_plural = 'Niveles Académicos'
		ordering = ['id']
	def __str__(self):
		return self.nombre

class Plataforma(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField('Nombre de la Plataforma', 
		max_length = 150)
	area = models.ManyToManyField(Area, 
		help_text='Seleccione las áreas de la plataforma.')
	nivel = models.ManyToManyField(Nivel, 
		help_text='Seleccione los niveles académicos ofrecidos por la plataforma.')
	objetivo = models.TextField('Objetivo de la Plataforma', 
		validators=[MaxLengthValidator(1000)])
	enlace = models.URLField('Enlace', max_length=255, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	fotografia = models.ImageField(upload_to = 'plataforma/', blank=True,
		help_text='Suba imágenes (jpg, gif, png).')
	fecha_de_creacion = models.DateField('Fecha de creación', auto_now_add=True)
	observaciones_sugerencias = models.TextField('Describa las observaciones y sugerencias', 
		validators=[MaxLengthValidator(1500)])
	ocultar = models.BooleanField('Plataforma descontinuada', default=False)
	class Meta:
		verbose_name_plural = 'Plataformas'
		ordering = ['id']
	def __str__(self):
		return self.nombre

class Enlace(models.Model):
	id = models.AutoField(primary_key = True)
	enlace = models.CharField('Enlace de la Herramienta', 
		max_length = 150)
	Descripcion = models.TextField('Descripción', 
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
	Descripcion = models.TextField('Descripción', 
		validators=[MaxLengthValidator(1000)])
	enlace = models.ForeignKey(Enlace, on_delete=models.PROTECT, 
		help_text='Seleccione el Enlace.')
	fotografia = models.ImageField(upload_to = 'plataforma/', 
		default='herramienta/image.jpg',
		help_text='Suba imágenes (jpg, gif, png).')
	fecha_de_creacion = models.DateField('Fecha de creación', auto_now_add=True)
	observaciones_sugerencias = models.TextField('Describa las observaciones y sugerencias', 
		validators=[MaxLengthValidator(1500)])
	ocultar = models.BooleanField('Herramienta descontinuada', default=False)
	class Meta:
		verbose_name_plural = 'Herramientas'
		ordering = ['id']
	def __str__(self):
		return self.nombre
