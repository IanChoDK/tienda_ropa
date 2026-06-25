from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tienda', views.ropa_list, name='ropa_list'),
    path("crear", views.crear_ropa, name="crear_ropa"),
    path("editar/<int:id>", views.editar_ropa, name="editar_ropa"),
    path("eliminar/<int:id>", views.eliminar_ropa, name="eliminar_ropa")
]