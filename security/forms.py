#!/usr/bin/env python
from django.forms import *

from .models import EstandarAcceso, Perfil, Persona


class BootrapModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BootrapModelForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_class()

    def set_bootstrap_class(self):
        for field in self.fields:
            try:
                self.fields[field].widget.attrs['class'] += ' form-group'
            except KeyError:
                self.fields[field].widget.attrs['class'] = 'form-group'


class EstandarAccesoForm(BootrapModelForm):

    class Meta:
        model = EstandarAcceso
        fields = ['nombre', 'descripcion', 'longitud_minima_clave', 'longitud_maxima_clave', 'complejidad_clave',
                  'vencimiento_clave', 'vencimiento_sesion', 'cantidad_accesos_fallidos']


class PerfilForm(BootrapModelForm):

    class Meta:
        model = Perfil
        fields = ['nombre', 'descripcion', 'estandar_acceso', 'permisos']


class PersonaForm(BootrapModelForm):

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'nombre_elegido', 'apellido_elegido']
