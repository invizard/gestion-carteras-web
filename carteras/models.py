
# Create your models here.
from django.db import models

# Tabla de entidades
class Entidad(models.Model):
    nombre = models.CharField(max_length=255)
    nit = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


# Tabla de pacientes
class Paciente(models.Model):
    tipo_identificacion = models.CharField(max_length=10)
    identificacion = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    afiliacion = models.CharField(max_length=50, null=True, blank=True)
    nivel_rango = models.CharField(max_length=10, null=True, blank=True)

# Tabla de contratos
class Contrato(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    nombre_contrato = models.CharField(max_length=255, null=True, blank=True)
    sede = models.CharField(max_length=100, null=True, blank=True)

# Tabla de facturas
class Factura(models.Model):
    numero_factura = models.CharField(max_length=50, unique=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_factura = models.DateField()
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_egreso = models.DateField(null=True, blank=True)
    valor_total_factura = models.DecimalField(max_digits=15, decimal_places=2)
    valor_copago = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_total_cobrar = models.DecimalField(max_digits=15, decimal_places=2)
    estado = models.CharField(max_length=50, null=True, blank=True)
    fecha_radicado = models.DateField(null=True, blank=True)
    numero_radicado = models.CharField(max_length=50, null=True, blank=True)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)

# Tabla de saldo (para seguimiento y actualización de facturas)
class Saldo(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE)  # Relación uno a uno con la factura
    valor_glosa = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    valor_glosa_aceptada = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    
    # Abono 1
    abono_1 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    retencion_1 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    fecha_abono_1 = models.DateField(null=True, blank=True)
    
    # Abono 2
    abono_2 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    retencion_2 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    fecha_abono_2 = models.DateField(null=True, blank=True)
    
    # Abono 3
    abono_3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    retencion_3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    fecha_abono_3 = models.DateField(null=True, blank=True)
    
    # Campo para el saldo total
    saldo_actual = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)

    def calcular_saldo(self):
        """Calcula el saldo actual de la factura."""
        total_abonos = (self.abono_1 - self.retencion_1) + (self.abono_2 - self.retencion_2) + (self.abono_3 - self.retencion_3)
        total_glosas = self.valor_glosa - self.valor_glosa_aceptada
        self.saldo_actual = self.factura.valor_total_cobrar - total_abonos - total_glosas
        self.save()
