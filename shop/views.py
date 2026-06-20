from django.shortcuts import render, redirect
from .models import Ropa
from .forms import RopaForm

# Create your views here.

def ropa_list(request):
    ropa = Ropa.objects.all()
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