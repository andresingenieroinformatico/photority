from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse




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





User = get_user_model()

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect

User = get_user_model()

def login(request):
    if request.method == 'POST':
        tipo_user = request.POST.get('tipo_user')  
        cedula = request.POST.get('cedula')
        contraseña = request.POST.get('contraseña')

        print("POST recibido:")
        print("tipo_user:", tipo_user)
        print("cedula:", cedula)
        print("contraseña:", contraseña)

        from django.contrib.auth import get_user_model
        from django.contrib.auth.hashers import check_password
        from django.contrib.auth import login as auth_login
        from django.contrib import messages

        User = get_user_model()

        try:
            user = User.objects.get(username=cedula)  # usamos username
            print("Usuario encontrado:", user)

            if check_password(contraseña, user.password):
                print("Contraseña válida")

                if user.role == tipo_user and user.role in ['Docente', 'Estudiante']:
                    auth_login(request, user)
                    print("Login exitoso")
                    return redirect('index')  # Asegúrate de que esta URL exista
                else:
                    messages.error(request, 'Rol no permitido.')
            else:
                print("Contraseña inválida")
                messages.error(request, 'Cédula o contraseña incorrectos.')
        except User.DoesNotExist:
            print("Usuario no encontrado")
            messages.error(request, 'Cédula o contraseña incorrectos.')

    return render(request, 'login.html')





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