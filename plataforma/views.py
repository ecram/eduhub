from django.shortcuts import render
from .models import *

from django.contrib.auth.decorators import login_required
from .forms import AreaForm

'''
from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'John'
user.last_name = 'Citizen'
user.save()
'''

# Create your views here.

@login_required
def plataforma(request):
	entradas = Plataforma.objects.all().exclude(ocultar=True)
	
	# Numero de visitas a esta view, como está contado en la variable de sesión.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	return render(request, 'plataforma.html', {'entradas':entradas, 
		'num_visits':num_visits,})


def post_new(request):
    form = AreaForm()
    return render(request, 'post_edit.html', {'form': form})

def error404(request, exception):
	return render(request,'error404.html', status=404)

def error500(request):
	return render(request,'error500.html', status=500)
