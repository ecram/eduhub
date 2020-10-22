from django.shortcuts import render
from .models import *

# Create your views here.
def herramienta(request):
	entradas = Herramienta.objects.all().exclude(ocultar=True)
	# Numero de visitas a esta view, como está contado en la variable de sesión.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1
	return render(request, 'herramienta.html', 
		{'entradas':entradas, 'num_visits':num_visits})