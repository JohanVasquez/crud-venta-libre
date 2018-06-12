# coding=utf-8
from django import forms
from .models import Ventas


class VentasForm(forms.ModelForm):
    """
    Autor: Johan Vasquez
    Fecha: 29/04/2018
    Descripción: Formulario para gestionar los sensores registrados en el sistema
    """

    class Meta:
        model = Ventas
        fields = ('producto', 'unidades_ventidas', 'fecha_venta')
