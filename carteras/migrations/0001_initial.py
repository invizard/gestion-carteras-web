# Generated by Django 5.1.3 on 2024-11-23 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('nit', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_identificacion', models.CharField(max_length=10)),
                ('identificacion', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('afiliacion', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel_rango', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_contrato', models.CharField(blank=True, max_length=255, null=True)),
                ('sede', models.CharField(blank=True, max_length=100, null=True)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carteras.entidad')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=50, unique=True)),
                ('fecha_factura', models.DateField()),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('fecha_egreso', models.DateField(blank=True, null=True)),
                ('valor_total_factura', models.DecimalField(decimal_places=2, max_digits=15)),
                ('valor_copago', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('valor_total_cobrar', models.DecimalField(decimal_places=2, max_digits=15)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_radicado', models.DateField(blank=True, null=True)),
                ('numero_radicado', models.CharField(blank=True, max_length=50, null=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carteras.contrato')),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carteras.entidad')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carteras.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_glosa', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('valor_glosa_aceptada', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('abono_1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('retencion_1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('fecha_abono_1', models.DateField(blank=True, null=True)),
                ('abono_2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('retencion_2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('fecha_abono_2', models.DateField(blank=True, null=True)),
                ('abono_3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('retencion_3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('fecha_abono_3', models.DateField(blank=True, null=True)),
                ('saldo_actual', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('factura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carteras.factura')),
            ],
        ),
    ]
