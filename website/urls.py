from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
	path('', views.home, name="home"),
	path('add.html', views.add, name="add"),
	path('substract.html', views.substract, name="substract"),
	path('multiply.html', views.multiply, name="multiply"),
	path('divide.html', views.divide, name="divide"),
]   