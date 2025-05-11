from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *

class UsuarioSaludViewSet(viewsets.ModelViewSet):
    queryset = UsuarioSalud.objects.all()
    serializer_class = UsuarioSaludSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ReporteClinicoViewSet(viewsets.ModelViewSet):
    queryset = ReporteClinico.objects.all()
    serializer_class = ReporteClinicoSerializer

class PrediccionAdversaViewSet(viewsets.ModelViewSet):
    queryset = PrediccionAdversa.objects.all()
    serializer_class = PrediccionAdversaSerializer

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class HistorialInteraccionViewSet(viewsets.ModelViewSet):
    queryset = HistorialInteraccion.objects.all()
    serializer_class = HistorialInteraccionSerializer
