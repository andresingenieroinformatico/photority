from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('reportar/', views.reportar, name='reportar'),
    path('reportes/', views.reportes, name='reportes'), 
    path('politicas_privacidad/', views.politicas_privacidad, name='politicas_privacidad'),
    path('terminos_condiciones/', views.politicas_privacidad, name='terminos_condiciones'), 
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'), 
    path('about/', views.about, name='about'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    ]
