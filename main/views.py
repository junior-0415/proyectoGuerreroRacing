from multiprocessing import context
from django.shortcuts import render

def inicio(request):
    context={}
    return render(request,'index.html',context)

def inicioAdmin(request):
    titulo="Panel Principal"
    context={
        'titulo':titulo
    }
    return render(request,'frm_inicio_app.html',context) 