from django.shortcuts import render
from contacto.templates.contacto import forms
# from contacto.models import contacto

# Create your views here.

def contacto(request):
    formulario = forms.FormularioContacto()  

    return render(request, "contacto/contacto.html", {'formulario': formulario})
    # ****************** no olvidar registrar la app en el archivo settings **************


