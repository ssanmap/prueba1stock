from django.shortcuts import render,redirect, HttpResponse

from .models import stock
# Create your views here.

def index(request):
    productos = stock.objects.all()
    context = {
        'productos':productos
    }
    return render(request, 'index.html',context)

def create(request):
    print(request.POST)
    title = request.GET['title']
    medida = request.GET['medida']
    productos_details = stock(title=title, medida=medida)
    productos_details.save()
    return redirect('/')
def add(request):
    return render(request,'add.html')

def delete(request, id):
    productos = stock.objects.get(pk=id)
    productos.delete()
    return redirect('/')

def edit(request, id):
    productos = stock.objects.get(pk=id)
    context = {
        'productos': productos
    }
    return render(request, 'edit.html', context)

def update(request, id):
    productos= stock.objects.get(pk=id)
    productos.title = request.GET['title']
    productos.medida = request.GET['medida']
    productos.price = request.GET['price']
    productos.save()
    return redirect('/')