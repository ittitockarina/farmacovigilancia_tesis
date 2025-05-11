from rest_framework import serializers
from .models import *

class UsuarioSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioSalud
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ReporteClinicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteClinico
        fields = '__all__'

class PrediccionAdversaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrediccionAdversa
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'

class HistorialInteraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialInteraccion
        fields = '__all__'
