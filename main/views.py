from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
    if request.method == 'POST':
        tipo_user = request.POST.get('tipo_user') 
        cedula = request.POST['cedula']
        contraseña = request.POST['contraseña']
        user = authenticate(request, cedula=cedula, contraseña=contraseña, tipo_user=tipo_user)
        if user is not None:
            try:
                profile = user.profile
                if profile.role in ['Admin', 'Docente', 'Estudiante']: 
                    login(request, user)
                    if profile.role == 'Admin':
                        return redirect('Admin_dashboard')
                    else:
                        return redirect('index.html')
                else:
                    messages.error(request, 'Rol no permitido.')
                    return render(request, 'login.html')
            except AttributeError:
                messages.error(request, 'El usuario no tiene un perfil asignado.')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
            return render(request, 'login.html')
    return render(request, 'index.html')


def registro(request):
    if request.method == 'POST':
        tipo_user = request.POST.get('tipo_user') 
        cedula = request.POST['cedula']
        contraseña = request.POST['contraseña']
        confirmacion_contraseña = request.POST['confirmacion_contraseña']
        
        if contraseña != confirmacion_contraseña:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'registro.html')
        
        # Aquí deberías agregar la lógica para crear el usuario y su perfil
        # Por ejemplo:
        # user = User.objects.create_user(username=cedula, password=contraseña)
        # profile = Profile.objects.create(user=user, role=tipo_user)
        
        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('login')
    
    return render(request, 'registro.html')