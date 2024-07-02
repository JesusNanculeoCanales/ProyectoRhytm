from django.shortcuts import render

# Create your views here.
def paginicio(request):
    return render(request,'rsound/Index.html')

def nosotros(request):
    return render(request,'rsound/Nosotros.html')

def listadoartistas(request):
    return render(request,'rsound/listadoArtistas.html')

def mercancia(request):
    return render(request,'rsound/Mercancia.html')

def novedades(request):
    return render(request,'rsound/Novedades.html')

def registro(request):
    return render(request,'rsound/registro.html')

def evento(request):
    return render(request,'rsound/evento.html')

def noticia(request):
    return render(request,'rsound/noticia.html')

def cerati(request):
    return render(request,'rsound/artistas/Gustavocerati.html')
def aespa(request):
    return render(request,'rsound/artistas/aespa.html')
def jungkook(request):
    return render(request,'rsound/artistas/jungkook.html')
def smiths(request):
    return render(request,'rsound/artistas/smiths.html')
def newjeans(request):
    return render(request,'rsound/artistas/newjeans.html')
def blur(request):
    return render(request,'rsound/artistas/blur.html')



