from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("tienda", views.ropa_list, name="ropa_list"),
    path("crear", views.crear_ropa, name="crear_ropa"),
    path("editar/<int:id>", views.editar_ropa, name="editar_ropa"),
    path("eliminar/<int:id>", views.eliminar_ropa, name="eliminar_ropa"),
    path("productos", views.ProductoListView.as_view(), name="producto_list"),
    path("productos/crear", views.ProductoCreateView.as_view(), name="crear_producto"),
    path(
        "productos/editar/<int:pk>",
        views.ProductoUpdateView.as_view(),
        name="editar_producto",
    ),
    path(
        "productos/eliminar/<int:pk>",
        views.ProductoDeleteView.as_view(),
        name="eliminar_producto",
    ),
]
