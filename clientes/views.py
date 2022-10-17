from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def clientes(request):
    context={

    }
    return render(request,'clientes/interfaz_clientes.html',context)