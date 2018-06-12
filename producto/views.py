# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import reverse

from .models import Ventas
from .forms import VentasForm


class VentasCreateView(CreateView):
    """
    Autor: Johan Vasquez - Cristian Viveros
    Descripción: Vista para crear ventas
    """
    model = Ventas
    form_class = VentasForm
    success_url = reverse_lazy('producto:listar_ventas')


class VentasUpdateView(UpdateView):
    """
    Autor: Johan Vasquez - Cristian Viveros
    Descripción: Vista para editar ventas
    """
    model = Ventas
    form_class = VentasForm
    success_url = reverse_lazy('producto:listar_ventas')


class VentasListView(ListView):
    """
    Autor: Johan Vasquez - Cristian Viveros
    Descripción: Vista para Listar ventas
    """
    model = Ventas


class VentasDelete(DeleteView):
    """
    Autor: Johan Vasquez - Cristian Viveros
    Descripción: Vista para eliminar las ventas
    """
    model = Ventas
    success_url = reverse_lazy('producto:listar_ventas')


class GraficaVentas(TemplateView):
    """
    Autor: Johan Vasquez - Cristian Viveros
    Descripción: Vista para eliminar las ventas
    """
    template_name = 'producto/estadistica.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GraficaVentas, self).get_context_data(*args, **kwargs)
        ventas = Ventas.objects.all()
        context['productos_ventido'] = ventas.count()
        cantidad_total = 0
        for venta in ventas:
            cantidad_total += venta.unidades_ventidas
        context['cantidad_total_vendida'] = cantidad_total
        return context

    def get_success_url(self):
        edit_url = reverse('contrato:reporte_personas_pdf')
        return edit_url