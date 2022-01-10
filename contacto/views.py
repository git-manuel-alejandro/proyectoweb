from django.shortcuts import render
# from contacto.models import contacto

# Create your views here.

def contacto(request):
    # servicios = Servcio.objects.all()
    saludo = 'hola mundo'

    return render(request, "contacto/contacto.html", {'saludo': saludo})
    # ****************** no olvidar registrar la app en el archivo settings **************


