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

def registrarse(request):
    mensaje={'mensaje':'te registraste'}
    return render(request,'rsound/Index.html',mensaje)

