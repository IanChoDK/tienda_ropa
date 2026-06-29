from django.shortcuts import render, redirect, get_object_or_404
from .models import Ropa, Producto
from .forms import RopaForm, ProductoForm

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


@login_required
@permission_required("shop.view_ropa")
def ropa_list(request):
    ropa = Ropa.objects.all().order_by("-id").filter(activo=True)
    return render(request, "ropa_list.html", {"ropa": ropa})


def inicio(request):
    return render(request, "inicio.html")


@login_required
@permission_required("shop.add_ropa")
def crear_ropa(request):
    if request.method == "POST":
        form = RopaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("ropa_list")
    else:
        form = RopaForm()
    return render(request, "crear_ropa.html", {"form": form})


@login_required
@permission_required("shop.change_ropa")
def editar_ropa(request, id):
    ropa = get_object_or_404(Ropa, id=id)

    if request.method == "POST":
        form = RopaForm(request.POST, request.FILES, instance=ropa)
        if form.is_valid():
            form.save()
            return redirect("ropa_list")
    else:
        form = RopaForm(instance=ropa)

    return render(request, "editar_ropa.html", {"form": form})


@login_required
@permission_required("shop.delete_ropa")
def eliminar_ropa(request, id):
    ropa = get_object_or_404(Ropa, id=id)
    if request.method == "POST":
        ropa.activo = False
        ropa.save()

        return redirect("ropa_list")
    return render(request, "eliminar_ropa.html", {"ropa": ropa})


class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "producto_list.html"
    context_object_name = "productos"
    ordering = ["-id"]

    def get_queryset(self):
        return self.model.objects.filter(stock__gt=0)


class ProductoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy("producto_list")
    permission_required = "shop.add_producto"


class ProductoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "editar_producto.html"
    success_url = reverse_lazy("producto_list")
    permission_required = "shop.change_producto"


class ProductoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Producto
    template_name = "eliminar_producto.html"
    success_url = reverse_lazy("producto_list")
    permission_required = "shop.delete_producto"
