from django.urls import path

from . import views

app_name = 'producto'
urlpatterns = [
    path('crear-venta', views.VentasCreateView.as_view(), name='crear_venta'),
    path('editar-venta/<int:pk>/', views.VentasUpdateView.as_view(), name='editar_venta'),
    path('', views.VentasListView.as_view(), name='listar_ventas'),
    path('eliminar-venta/<int:pk>/', views.VentasDelete.as_view(), name='eliminar_venta'),
    path('grafica-venta', views.GraficaVentas.as_view(), name='grafica_venta'),
]
