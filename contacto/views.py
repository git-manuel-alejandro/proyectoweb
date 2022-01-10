from django.shortcuts import redirect, render
from contacto.templates.contacto import forms
# from contacto.models import contacto

# Create your views here.

def contacto(request):
    formulario = forms.FormularioContacto()  

    if request.method == "POST":
        formulario = forms.FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            return redirect("/contacto/?valido")


    return render(request, "contacto/contacto.html", {'formulario': formulario})
    # ****************** no olvidar registrar la app en el archivo settings **************


