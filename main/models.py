from django.db import models

class usuarios(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    tipo_user = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=100)