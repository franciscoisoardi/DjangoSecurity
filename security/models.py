#!/usr/bin/env python
from django.contrib.auth.models import User, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


TIPO_CONTACTO_CHOICES = (
    0, 'Mail',
    1, 'Teléfono',
)

TIPO_DOCUMENTO_CHOICES = (
    0, 'DNI',
    1, 'LC',
    2, 'LE',
    3, 'Pasaporte',
)


class Perfil(models.Model):

    nombre = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_('Nombre')
    )
    descripcion = models.TextField(
        null=False, blank=False, verbose_name=_('Descripción')
    )
    permisos = models.ManyToManyField(
        Permission, null=False, blank=False, verbose_name=_('Permisos')
    )


class Contacto(models.Model):

    contacto = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_('Contacto')
    )
    tipo = models.SmallIntegerField(
        null=False, blank=False, verbose_name=_('Tipo de Contacto')
    )


class Documento(models.Model):

    numero = models.CharField(
        max_length=50, null=False, blank=False, verbose_name=_('Número de Documento')
    )
    tipo = models.SmallIntegerField(
        null=False, blank=False, verbose_name=_('Tipo de Documento')
    )


class Persona(models.Model):

    nombre = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_('Nombres')
    )
    apellido = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_('Apellido')
    )
    nombre_elegido = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_('Nombres Elegidos')
    )
    apellido_elegido = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_('Apellidos Elegidos')
    )
    contactos = models.ManyToManyField(
        Contacto, null=True, blank=True, verbose_name=_('Contactos')
    )
    documentos = models.ManyToManyField(
        Documento, null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Documentos')
    )
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
