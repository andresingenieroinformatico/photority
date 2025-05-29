from django.shortcuts import render
from django.http import Http404

def inicio(request):
    return render(request, 'inicio.html') 

def reportar(request):
    return render(request, 'reportar.html')

def reportes(request):
    return render(request, 'reportes.html')

def politicas_privacidad(request):
    return render(request, 'politicas_privacidad.html')

def quienes_somos(request):                 
    return render(request, 'quienes_somos.html') 

def contacto(request):
    return render(request, 'contacto.html')     

def terminos_condiciones(request):
    return render(request, 'terminos_condiciones.html')

def about(request):
    return render(request, 'about.html') 

def login(request):
    return render(request, 'login.html') 