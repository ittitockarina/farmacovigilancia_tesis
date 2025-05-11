"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect

# Vista para la raíz "/"
def home_view(request):
    return HttpResponse("Bienvenido a la página principal.")

# Vista temporal para probar la API (si no tienes aún)
def api_home(request):
    return HttpResponse("Bienvenido al API.")

urlpatterns = [
    path('', home_view, name='home'),                  # Ruta raíz: muestra bienvenida
    path('admin/', admin.site.urls),                   # Panel admin
    path('api/', api_home, name='api-home'),           # Vista temporal para /api/
]

