from django.urls import path
from contacto import views

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [    
    path('', views.contacto , name="Contacto"),
    # no olvidar registrar la app en el archivo settings

]