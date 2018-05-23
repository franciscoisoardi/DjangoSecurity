#!/usr/bin/env python
from django.forms import *

from .models import EstandarAcceso, Perfil, Persona


class EstandarAccesoForm(ModelForm):

    class Meta:
        model = EstandarAcceso
        fields = ['nombre', 'descripcion', 'longitud_minima_clave', 'longitud_maxima_clave', 'complejidad_clave',
                  'vencimiento_clave', 'vencimiento_sesion', 'cantidad_accesos_fallidos']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-group'}),
            'descripcion': Textarea(attrs={'class': 'form-group'}),
            'longitud_minima_clave': TextInput(attrs={'class': 'form-group'}),
            'longitud_maxima_clave': TextInput(attrs={'class': 'form-group'}),
            'complejidad_clave': TextInput(attrs={'class': 'form-group'}),
            'vencimiento_clave': TextInput(attrs={'class': 'form-group'}),
            'vencimiento_sesion': TextInput(attrs={'class': 'form-group'}),
            'cantidad_accesos_fallidos': TextInput(attrs={'class': 'form-group'}),
        }


class PerfilForm(ModelForm):

    class Meta:
        model = Perfil
        fields = ['nombre', 'descripcion', 'estandar_acceso', 'permisos']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-group'}),
            'descripcion': Textarea(attrs={'class': 'form-group'}),
            'estandar_acceso': Select(attrs={'class': 'form-group'}),
            'permisos': SelectMultiple(attrs={'class': 'form-group'}),
        }


class PersonaForm(ModelForm):

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'nombre_elegido', 'apellido_elegido']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-group'}),
            'apellido': Textarea(attrs={'class': 'form-group'}),
            'nombre_elegido': Select(attrs={'class': 'form-group'}),
            'apellido_elegido': SelectMultiple(attrs={'class': 'form-group'}),
        }
