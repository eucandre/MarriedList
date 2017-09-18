from django.shortcuts import render
from .forms import *

def inicio(request):
    return render(request,'index.html')

def casamentos_inicio(request):
    if request.method =='POST':
        form = FormCasal(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormCasal()
    return render(request,'casal/index_casal.html', {'form':form})

def desejos_insere(request):
    if request.method =='POST':
        form = FormDesejos(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormDesejos()
    return render(request,'Desejos/index_desejos.html', {'form':form})