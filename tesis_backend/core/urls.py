from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('usuarios', UsuarioSaludViewSet)
router.register('pacientes', PacienteViewSet)
router.register('reportes', ReporteClinicoViewSet)
router.register('predicciones', PrediccionAdversaViewSet)
router.register('alertas', AlertaViewSet)
router.register('interacciones', HistorialInteraccionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
