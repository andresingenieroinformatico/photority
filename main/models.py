from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    tipo_user = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Reporte(models.Model):
    TIPO_DANO_CHOICES = [
        ('fisico', 'Físico'),
        ('tecnologico', 'Tecnológico'),
    ]

    PRIORIDAD_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]
    id_reporte = models.AutoField(primary_key=True)
    tipo_dano = models.CharField(max_length=20, choices=TIPO_DANO_CHOICES)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)  
    imagen = models.ImageField(upload_to='reportes/', null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_dano} - {self.usuario.nombre} ({self.fecha.date()})"

class ReporteAdmin(admin.ModelAdmin):
    list_display = ('id_reporte', 'tipo_dano', 'descripcion','prioridad','usuario','fecha','imagen', 'ver_link')
    list_filter = ('tipo_dano', 'prioridad', 'fecha')
    search_fields = ('descripcion', 'usuario__nombre')
    readonly_fields = ('imagen_preview',)

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 80px;" />', obj.imagen.url)
        return "Sin imagen"
    imagen_preview.short_description = 'Imagen'

    def ver_link(self, obj):
        url = reverse("admin:main_reporte_change", args=[obj.id_reporte])
        return format_html('<a class="button" href="{}">Ver</a>', url)
    ver_link.short_description = "Acciones"