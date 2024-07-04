from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from .forms import ArtistaForm, RegistroForm, LoginForm
from .models import Artista, Usuario, Rol
from django.contrib.auth.models import User

def paginicio(request):
    return render(request, 'rsound/Index.html')

def nosotros(request):
    return render(request, 'rsound/Nosotros.html')

def listadoartistas(request):
    artistas = Artista.objects.all()
    return render(request, 'rsound/listadoArtistas.html', {'artistas': artistas})

def mercancia(request):
    return render(request, 'rsound/Mercancia.html')

def novedades(request):
    return render(request, 'rsound/Novedades.html')

def registro(request):
    return render(request, 'rsound/registro.html')

def evento(request):
    return render(request, 'rsound/evento.html')

def noticia(request):
    return render(request, 'rsound/noticia.html')

def cerati(request):
    return render(request, 'rsound/artistas/Gustavocerati.html')

def aespa(request):
    return render(request, 'rsound/artistas/aespa.html')

def jungkook(request):
    return render(request, 'rsound/artistas/jungkook.html')

def smiths(request):
    return render(request, 'rsound/artistas/smiths.html')

def newjeans(request):
    return render(request, 'rsound/artistas/newjeans.html')

def blur(request):
    return render(request, 'rsound/artistas/blur.html')

def administracion(request):
    return render(request, 'rsound/Admin/administracion.html')

def adminartistas(request):
    return render(request, 'rsound/Admin/adminArtistas.html')

def adminusuario(request):
    return render(request, 'rsound/Admin/adminUsuario.html')

def listado_usuario(request):

    roles=Rol.objects.all()
    usuario=Usuario.objects.all()
    contexto={
        "roles":roles,
        "persona":usuario
    }
    return render(request, 'rsound/Admin/listado_usuario.html',contexto)


def crear_usuario(request):
    roles=Rol.objects.all()
    contexto={
        "roles":roles
    }
    return render(request, 'rsound/Admin/crear_usuario.html',contexto)


## funciones

def crear_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoartistas')
    else:
        form = ArtistaForm()
    return render(request, 'rsound/admin/crear_artista.html', {'form': form})

def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('listadoartistas')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'rsound/admin/editar_artista.html', {'form': form})

def eliminar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('listadoartistas')
    return render(request, 'rsound/admin/eliminar_artista.html', {'object': artista})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                form.add_error(None, "Correo o contraseña incorrectos.")
    else:
        form = LoginForm()
    return render(request, 'rsound/Index.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio')

def registrar_usuario(request):
    nombreUsu = request.POST['nickname']         
    nombres= request.POST['name'] 
    apellido = request.POST['apellido'] 
    correoU   = request.POST['email'] 
    claveU    = request.POST['password'] 
    telefonoU = request.POST['telefono']
    rol=Rol.objects.get(nombreRol="Usuario")

    usuario=Usuario.objects.create(
        nombreUsuario=nombreUsu,
        nombre=nombres,
        apellidos=apellido,
        correo=correoU,
        contraseña=claveU,
        numero_telefonico=telefonoU,
        fechacreacion=timezone.now(),
        rol=rol
    )

    user = User.objects.create_user(
        username = correoU,
        email = correoU,
        password = claveU
    )
    user.first_name = nombreUsu
    user.last_name = apellido
    user.is_staff=False
    user.save()


    return redirect('inicio')











