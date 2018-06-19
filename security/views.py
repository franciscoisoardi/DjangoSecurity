#!/usr/bin/env python
import operator
from functools import reduce

from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import EstandarAcceso, Perfil, Persona


class GenericListView(ListView):

    model = object
    search_terms = None
    # Cada término debe comenzar con + si es numérico y * si es caracter. No se admiten otros valores (aún).
    search_fields = ()

    def get_search_terms(self):
        """
        Devuelve una lista con los términos de búsqueda.
        :return: List
        """
        return self.search_terms.split()

    def construct_search(self, field):
        """
        Arma la condición de filtro para un campo determinado.
        :param field:
        :return: String
        """
        if self.search_fields[0] == '+':
            return field + '__icontains'
        elif self.search_fields[0] == '*':
            return field + '__unaccent__icontains'
        else:
            return field + '__icontains'

    def filter_queryset(self, queryset):
        """
        Devuelve el queryset filtrado por los términos de búsqueda y los campos seteados.
        :param queryset:
        :return: Queryset
        """
        search_terms = self.get_search_terms()
        search_fields = [self.construct_search(field) for field in self.search_fields]
        for search_term in search_terms:
            term = search_term.replace('-', '') if search_term[0] == '-' else search_term
            conditions = []
            queries = [Q(**{search_field: term}) for search_field in search_fields]
            conditions.append(reduce(operator.or_, queries))
            if search_term[0] == '-':
                queryset = queryset.exclude(reduce(operator.and_, conditions))
            else:
                queryset = queryset.filter(reduce(operator.and_, conditions))
        return queryset

    def get_queryset(self):
        """
        Devuelve los objetos del modelo de la vista, y realiza un filtro si hay términos de búsqueda.
        :return: QuerySet
        """
        queryset = self.model.objects.all()
        self.search_terms = self.request.GET.get('search', None)
        if self.search_terms:
            queryset = self.filter_queryset(queryset)
        return queryset


class GenericCreateView(CreateView):

    pass


class GenericUpdateView(UpdateView):

    pass


class GenericDeleteView(DeleteView):

    pass


class EstandarAccesoListView(GenericListView):

    model = EstandarAcceso
    search_fields = ('*nombre', '*descripcion')


class PerfilListView(GenericListView):

    model = Perfil
    search_fields = ('*nombre', '*descripcion')


class PersonaListView(GenericListView):

    model = Persona
    search_fields = ('*nombre', '*descripcion')
