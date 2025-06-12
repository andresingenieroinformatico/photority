from django.contrib import admin
from .models import Usuario, Reporte, ReporteAdmin

admin.site.register(Usuario)
admin.site.register(Reporte, ReporteAdmin)


