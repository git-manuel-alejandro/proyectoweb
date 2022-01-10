from django.shortcuts import render
from servicios.models import Servcio

# Create your views here.

def servicios(request):
    servicios = Servcio.objects.all()

    return render(request, "servicios/servicios.html", {'servicios' : servicios})
