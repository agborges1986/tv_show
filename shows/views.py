from django.shortcuts import render,HttpResponse,redirect
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    return redirect('/shows')

def show(request):
    shows=Show.objects.all()
    context = {
        'shows': shows,
    }
    return render(request, 'show.html',context=context)

def new(request):
    return render(request, 'new.html')

def create(request):
    print(request.POST)
    show=Show.objects.create(titulo=request.POST['titulo'],productor=request.POST['productor'],lanzamiento=datetime.strptime(request.POST['lanzamiento'], "%Y-%m-%d"),descripcion=request.POST['descripcion'])
    context = {
        'show':show
    }
    return redirect(f'/shows/{show.id}')

def show_id(request,id):
    show=Show.objects.get(id=id)
    context={
        "show":show
    }
    return render(request,"showid.html",context=context)

def delete_id(request,id):
    show=Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

def edit(request):
    show=Show.objects.get(id=request.POST['id'])
    show.titulo=request.POST['titulo']
    show.productor=request.POST['productor']
    show.descripcion=request.POST['descripcion']
    show.lanzamiento=datetime.strptime(request.POST['lanzamiento'], "%Y-%m-%d")
    show.save()
    return redirect('/shows') 

def edit_id(request,id):
    show=Show.objects.get(id=id)
    context={
        "show":show
    }
    return render(request,"edit.html",context=context)  
