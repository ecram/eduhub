from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.plataforma, name='index'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('post/new', views.post_new, name='post_new'),
]