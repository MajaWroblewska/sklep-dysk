"""DjangoSklep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from sklepApp.views import MojeLogwanie
from sklepApp.views import (ProduktView, ProduktCreateView, ProduktUpdateView, ProduktDeleteView, \
    ProduktSelectUpdateView, ProduktSelectDeleteView )
from sklepApp.views import (KategoriaView, KategoriaCreateView, KategoriaUpdateView, KategoriaDeleteView, \
    KategoriaSelectUpdateView, KategoriaSelectDeleteView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', MojeLogwanie.as_view(), name='login'),

    path('produkt/', ProduktView.as_view(), name='produkt'),
    path('produkt/create', ProduktCreateView.as_view(), name='produkt_create'),
    path('produkt/update/<pk>', ProduktUpdateView.as_view(), name='produkt_update'),
    path('produkt/update', ProduktSelectUpdateView.as_view(), name='select_produkt_update'),
    path('produkt/delete/<pk>', ProduktDeleteView.as_view(), name='produkt_delete'),
    path('produkt/delete', ProduktSelectDeleteView.as_view(), name='select_produkt_delete'),

    path('kategoria/', KategoriaView.as_view(), name='kategoria'),
    path('kategoria/create', KategoriaCreateView.as_view(), name='kategoria_create'),
    path('kategoria/update/<pk>', KategoriaUpdateView.as_view(), name='kategoria_update'),
    path('kategoria/update', KategoriaSelectUpdateView.as_view(), name='select_kategoria_update'),
    path('kategoria/delete/<pk>', KategoriaDeleteView.as_view(), name='kategoria_delete'),
    path('kategoria/delete', KategoriaSelectDeleteView.as_view(), name='select_kategoria_delete'),



]
