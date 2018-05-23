#!/usr/bin/env python
from django.contrib.auth.models import User, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


COMPLEJIDAD_CLAVE_CHOICES = (
    0, 'Libre',
    1, 'Al menos una mayúscula y una minúscula',
    2, 'Al menos una mayúscula, una minúscula y un número',
    3, 'Al menos una mayúscula, una minúscula, un número y un sibolo',
)

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


class EstandarAcceso(models.Model):

    nombre = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_('Nombre')
    )
    descripcion = models.TextField(
        null=False, blank=False, verbose_name=_('Descripción')
    )
    longitud_minima_clave = models.SmallIntegerField(
        null=False, blank=False, verbose_name=_('Longitud mínima de contraseña'),
        help_text=_('Longitud mínima que debe tener la contraseña')
    )
    longitud_maxima_clave = models.SmallIntegerField(
        null=False, blank=False, verbose_name=_('Longitud máxima de contraseña'),
        help_text=_('Longitud máxima que puede tener la contraseña')
    )
    complejidad_clave = models.SmallIntegerField(
        null=False, blank=False, choices=COMPLEJIDAD_CLAVE_CHOICES, verbose_name=_('Complejidad de la contraseña'),
        help_text=_('Complejidad que debe tener la contraseña')
    )
    vencimiento_clave = models.SmallIntegerField(
        null=False, blank=False, verbose_name=_('Vencimiento de la contraseña'),
        help_text=_('Tiempo máximo de vigencia de la contraseña (expresado en días corridos) antes de forzar su cambio')
    )
    vencimiento_sesion = models.IntegerField(
        null=False, blank=False, verbose_name=_('Tiempo de vencimiento de sesión'),
        help_text=_('Tiempo máximo de inactividad antes de cierre de sesión automática')
    )
    cantidad_accesos_fallidos = models.SmallIntegerField(
        null=False, blank=False, verbose_name=_('Cantidad de intentos fallídos de acceso'),
        help_text=_('Cantidad de intentos fallidos de acceso consecutivos antes de bloquear el usuario')
    )


class Perfil(models.Model):

    nombre = models.CharField(
        max_length=200, null=False, blank=False, verbose_name=_('Nombre')
    )
    descripcion = models.TextField(
        null=False, blank=False, verbose_name=_('Descripción')
    )
    estandar_acceso = models.ForeignKey(
        EstandarAcceso, null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Estandar de Acceso')
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
        User, null=False, blank=False, on_delete=models.CASCADE, verbose_name=_('Usuario')
    )
