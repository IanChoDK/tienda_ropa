from django.urls import path
from . import views

urlpatterns = [
    path('', views.ropa_list, name='ropa_list'),
]