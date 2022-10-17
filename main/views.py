from multiprocessing import context
from django.shortcuts import render

def inicio(request):
    context={}
    return render(request,'index.html',context)

def inicioAdmin(request):
    context={

    }
    return render(request,'frm_inicio_app.html',context) 