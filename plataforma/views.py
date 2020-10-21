from django.shortcuts import render
from .models import *


# Create your views here.
def plataforma(request):
	entradas = Plataforma.objects.all().exclude(ocultar=True)
	return render(request, 'plataforma.html', {'entradas':entradas})
