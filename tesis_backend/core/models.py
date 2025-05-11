from django.db import models

class UsuarioSalud(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.TextField()
    especialidad = models.CharField(max_length=100)

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    dni = models.CharField(max_length=8, unique=True)
    sexo = models.CharField(max_length=10)
    direccion = models.TextField()
    historia_clinica = models.CharField(max_length=100)
    tipo_cancer = models.CharField(max_length=100)
    estadio = models.CharField(max_length=50)
    fecha_diagnostico = models.DateField()
    tratamiento_actual = models.TextField()
    usuario = models.ForeignKey(UsuarioSalud, null=True, on_delete=models.SET_NULL)

class ReporteClinico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    resumen = models.TextField()
    creado_por = models.ForeignKey(UsuarioSalud, null=True, on_delete=models.SET_NULL)

class PrediccionAdversa(models.Model):
    reporte = models.ForeignKey(ReporteClinico, on_delete=models.CASCADE)
    riesgo = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_reaccion = models.CharField(max_length=150)
    fecha_prediccion = models.DateTimeField()

class Alerta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nivel_riesgo = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha_alerta = models.DateTimeField()
    generada_por = models.ForeignKey(UsuarioSalud, null=True, on_delete=models.SET_NULL)

class HistorialInteraccion(models.Model):
    usuario = models.ForeignKey(UsuarioSalud, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    accion = models.TextField()
    fecha = models.DateTimeField()
