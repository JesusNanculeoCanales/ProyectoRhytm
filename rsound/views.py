from django.shortcuts import render

# Create your views here.
def paginicio(request):
    return render(request,'rsound/Index.html')

def nosotros(request):
    return render(request,'rsound/Nosotros.html')

def listadoartistas(request):
    return render(request,'rsound/listadoArtistas.html')

def cerati(request):
    return render(request,'rsound/artistas/Gustavocerati.html')

def mercancia(request):
    return render(request,'rsound/Mercancia.html')

def novedades(request):
    return render(request,'rsound/Novedades.html')

def registro(request):
    return render(request,'rsound/registro.html')



