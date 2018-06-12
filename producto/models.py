from django.db import models


class Ventas(models.Model):
    """
    Autor: Johan Vasquez - Cristian Viveros
    Descrición: Este modelo utiliza el ORM de Djangome que genera Query para crear esta
                tabla en la Base de Datos Mysql
    """
    producto = models.CharField(max_length=200)
    unidades_ventidas = models.IntegerField()
    fecha_venta = models.DateField('Fecha de venta (AAAA-mm-dd)')

    def __str__(self):
        return self.producto, self.fecha_venta
