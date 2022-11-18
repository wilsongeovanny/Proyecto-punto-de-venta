#---------- Importaciones de librerias / paquetes -----------

from django.shortcuts import render

#---------- Create your views here. -------------------------

#todo------------ Pagina de inicio principal ----------------

def index_home(request):
    return render(request, 'home/index_home.html')