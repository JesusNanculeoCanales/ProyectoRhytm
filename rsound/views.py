from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from .forms import ArtistaForm, RegistroForm, LoginForm
from .models import Artista, Usuario, Rol
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def paginicio(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)

    contexto = {
        "es_admin": es_admin
    }

    return render(request, 'rsound/Index.html', contexto)

def nosotros(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)

    contexto = {
        "es_admin": es_admin
    }
    return render(request, 'rsound/Nosotros.html', contexto)

def listadoartistas(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)

    artistas = Artista.objects.all()
    contexto = {
        "es_admin": es_admin,
        'artistas': artistas
    }
    return render(request, 'rsound/listadoArtistas.html', contexto)
    

def mercancia(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)

    contexto = {
        "es_admin": es_admin
    }
    return render(request, 'rsound/Mercancia.html', contexto)

def novedades(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)

    contexto = {
        "es_admin": es_admin
    }
    return render(request, 'rsound/Novedades.html', contexto)

def registro(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)

    contexto = {
        "es_admin": es_admin
    }
    return render(request, 'rsound/registro.html',contexto)

def evento(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)

    contexto = {
        "es_admin": es_admin
    }
    return render(request, 'rsound/evento.html',contexto)


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

def adminevento(request):
    return render(request, 'rsound/Admin/adminEvento.html')

def crear_artista(request):
    return render(request, 'rsound/Admin/crear_artista.html')


def listado_artista(request):
    artista=Artista.objects.all()
    contexto={
        "arte":artista
    }
    return render(request, 'rsound/Admin/listado_artista.html',contexto)

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

def pagEditar_usuario(request, id_usuario):

    usuarioAEditar = Usuario.objects.get(idUsuario = id_usuario) 
    roles = Rol.objects.all()

    contexto = {
        "id_usuario": id_usuario,
        "usuario": usuarioAEditar,
        "roles": roles
    }
    return render(request, 'rsound/Admin/editar_usuario.html', contexto)

## funciones



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

    Usuario.objects.create(
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


def registrar_usuario_admin(request):

    nombreUsu = request.POST['nickname']         
    nombres= request.POST['name'] 
    apellido = request.POST['apellido'] 
    correoU   = request.POST['email'] 
    claveU    = request.POST['password'] 
    telefonoU = request.POST['telefono']
    rol = request.POST['rol']

    rolModels = Rol.objects.get(idRol = rol)

    Usuario.objects.create(
        nombreUsuario=nombreUsu,
        nombre=nombres,
        apellidos=apellido,
        correo=correoU,
        contraseña=claveU,
        numero_telefonico=telefonoU,
        fechacreacion=timezone.now(),
        rol=rolModels
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

    return redirect('adminusuario')




def registrar_artista(request):
    nombreArt = request.POST['nameartista']         
    image= request.FILES.get('imagen',None)
    biografia = request.POST['biografia'] 
    discografia= request.POST['discos'] 
    recopilatorio= request.POST.get('recopilatorio',None) 
    videos = request.POST['video']

    artista=Artista.objects.create(
        nombreArtista= nombreArt,
        imagen = image,
        biografiaArtista=biografia,
        discografiaArtista=discografia,
        recopilatorioArtista=recopilatorio,
        video = videos
    )
    return redirect('administracion')


def eliminar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('adminartistas')
    return render(request, 'rsound/Admin/eliminar_artista.html', {'artista': artista})

def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.nombreArtista = request.POST['nameartista']
        if 'imagen' in request.FILES:
            artista.imagen = request.FILES['imagen']
        artista.biografiaArtista = request.POST['biografia']
        artista.discografiaArtista = request.POST['discos']
        artista.recopilatorioArtista = request.POST['recopilatorio']
        artista.video = request.POST['video']
        artista.save()
        return redirect('adminartistas')
    return render(request, 'rsound/Admin/editar_artista.html', {'artista': artista})

def editar_usuario_funcion(request, id_usuario):
    try:
        nombre=request.POST['name']
        apellido=request.POST['apellido']
        nombreusuario=request.POST['nickname']
        emails=request.POST['email']
        telefonos=request.POST['telefono']
        contrasena=request.POST.get('password',None)
        rol = request.POST['rol']

        #EDITAR TABLA USUARIOS

        usuarios = Usuario.objects.get(idUsuario = id_usuario)
        usuarios.nombreUsuario = nombreusuario
        usuarios.apellidos =  apellido
        usuarios.nombre = nombre
        usuarios.correo = emails
        usuarios.numero_telefonico = telefonos
        if contrasena:
            usuarios.contraseña = contrasena
        usuarios.rol = Rol.objects.get(idRol = rol)
        usuarios.save()

        #EDITAR TABLA USERS
        userDjango = User.objects.get(username = emails)
        userDjango.email= emails
        userDjango.username = emails
        userDjango.first_name= nombreusuario
        userDjango.last_name= apellido

        #VALIDAR STAFF
        userDjango.is_staff = False
        if rol == 2:
            userDjango.is_staff = True

        userDjango.save()
        messages.success(request, 'Editado Correctamente.')
    
    except Exception as e:
        messages.error(request, 'Ocurrio un Error.')

    return redirect('listado_usuario')


def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('adminusuario')
    return render(request, 'rsound/admin/eliminar_usuario.html', {'usuario': usuario})


def eliminar_usuario(request, id_usuario):

    #OBTENER USUARIO MODELS
    usuario = Usuario.objects.get(idUsuario = id_usuario)

    #OBTENER USUARIO DJANGO
    userDjango = User.objects.get(username = usuario.correo)

    #ELIMINAR USER DJANGO
    userDjango.delete()

    #ELIMINAR USUARIO MODELS
    usuario.delete()

    return redirect('listado_usuario')


def iniciar_sesion(request):
        
    usuario1 = request.POST.get('usuario','')
    contra1 = request.POST.get('contra','')
    if not usuario1:
        return redirect('inicio')
    
    try: 
        user1 = User.objects.get(username = usuario1)
    except User.DoesNotExist:
        messages.error(request, 'El usuario o la contraseña son incorrectas')
        return redirect('inicio')

    pass_valida = check_password(contra1, user1.password)
    if not pass_valida:
        messages.error(request, 'El usuario o la contraseña son incorrectas')
        return redirect('inicio')

    usuario2 = Usuario.objects.get(correo = usuario1)
    user = authenticate(username = usuario1, password=contra1)

    if user is not None:
        login(request, user)
        if(usuario2.rol.nombreRol == "Admin"):
            usuario2.is_staff=True
            usuario2.save
            return redirect('administracion')
        
        else: 
            usuario2.is_staff=False
            usuario2.save

            return redirect('inicio')
    else:
        return redirect('inicio')





#FUNCION EXTRA
def es_admin_funcion(request):
    user = request.user
    username = user.username

    usuarioModel = Usuario.objects.get(correo = username)
    rolModel = usuarioModel.rol

    if rolModel.nombreRol == 'Admin':
        es_admin = True
    else:
        es_admin = False

    return es_admin

