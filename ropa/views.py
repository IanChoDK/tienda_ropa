from django.shortcuts import render
from ropa.models import Ropa

# Create your views here.

def ropa_list(request):
    ropa = Ropa.objects.all()
    return render(request, 'ropa_list.html', {'ropa': ropa})