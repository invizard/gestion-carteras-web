from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Factura, Saldo, Paciente, Entidad, Contrato

admin.site.register(Factura)
admin.site.register(Saldo)
admin.site.register(Paciente)
admin.site.register(Entidad)
admin.site.register(Contrato)
