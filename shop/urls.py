from django.urls import path
from . import views

urlpatterns = [
    path('', views.ropa_list, name='ropa_list'),
    path("crear", views.crear_ropa, name="crear_ropa"),
]