from django.shortcuts import render, redirect, get_object_or_404
from .models import Ropa
from .forms import RopaForm

# Create your views here.

def ropa_list(request):
    ropa = Ropa.objects.all().order_by("-id").filter(activo=True)
    return render(request, "ropa_list.html", {"ropa": ropa})

def crear_ropa(request):
    if request.method == "POST":
        form = RopaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("ropa_list")
    else:
        form = RopaForm()
    return render(request, "crear_ropa.html", {"form": form})

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

def eliminar_ropa(request,id):
    ropa = get_object_or_404(Ropa, id=id)
    if request.method == "POST":
        ropa.activo = False
        ropa.save()

        return redirect("ropa_list")
    return render(request, "eliminar_ropa.html", {"ropa": ropa})