"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path

def v_home(request):
    return HttpResponse('home view return')

def v_about(request):
    return HttpResponse('about view return')

def v_contact(request):
    return HttpResponse('contact view return')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v_home),
    path('about/', v_about),
    path('contact/', v_contact),
]
