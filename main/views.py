from django.contrib import messages
from .models import Usuario, Reporte
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reporte
from django.shortcuts import render, redirect, get_object_or_404



def inicio(request):
    return render(request, 'inicio.html') 

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
    if request.method == 'POST':
        tipo_user = request.POST.get('tipo_user')
        cedula = request.POST.get('cedula')
        contraseña = request.POST.get('contraseña')
        try:
            usuario = Usuario.objects.get(cedula=cedula, contraseña=contraseña, tipo_user=tipo_user)
            request.session['id_user'] = usuario.id_user
            return redirect('index')  
        except Usuario.DoesNotExist:
            messages.error(request, 'Cédula o contraseña incorrectos')
    return render(request, 'login.html')

def index(request):
    if not request.session.get('id_user'): 
        return redirect('login')
    usuario = Usuario.objects.get(id_user=request.session['id_user']) 
    return render(request, 'index.html', {'usuario': usuario})


def mi_perfil(request):
    return render(request, 'mi_perfil.html')

def logout(request):
    request.session.flush()  
    return redirect('login') 

def reportar(request): 
    if not request.session.get('id_user'):
        return redirect('login')  
    usuario = get_object_or_404(Usuario, id_user=request.session['id_user'])
    if request.method == 'POST':
        tipo_dano = request.POST.get('tipo_dano', '').strip()
        descripcion = request.POST.get('descripcion', '').strip()
        prioridad = request.POST.get('prioridad', '').strip()
        imagen = request.FILES.get('imagen')  
        if not tipo_dano or not descripcion or not prioridad:
            messages.error(request, 'Todos los campos son obligatorios.')
        else:
            Reporte.objects.create(
                usuario=usuario,
                tipo_dano=tipo_dano,
                descripcion=descripcion,
                prioridad=prioridad,
                imagen=imagen
            )
            messages.success(request, 'El reporte ha sido enviado exitosamente.')
            return redirect('reportar')
    return render(request, 'reportar.html', {'usuario': usuario})

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        correo = request.POST.get('correo')
        tipo_user = request.POST.get('tipo_user')
        contraseña = request.POST.get('contraseña')
        confirmacion_contraseña = request.POST.get('confirmacion_contraseña')
        if contraseña != confirmacion_contraseña:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'registro.html')
        if Usuario.objects.filter(cedula=cedula).exists():
            messages.error(request, 'La cédula ya está registrada.')
            return render(request, 'registro.html')
        if not correo:
            messages.error(request, "El campo correo está llegando vacío.")
            return render(request, 'registro.html')
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            correo=correo,
            tipo_user=tipo_user,
            contraseña=contraseña 
        )
        nuevo_usuario.save()
        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('login')
    return render(request, 'registro.html')


def reportes(request):
    if not request.session.get('id_user'):
        return redirect('login')
    usuario = Usuario.objects.get(id_user=request.session['id_user'])
    reportes = Reporte.objects.filter(usuario=usuario) 
    return render(request, 'reportes.html', {'usuario': usuario, 'reportes': reportes})


def mi_perfil(request):
    if not request.session.get('id_user'):
        return redirect('login')
    usuario = Usuario.objects.get(id_user=request.session['id_user'])
    return render(request, 'mi_perfil.html', {'usuario': usuario})
