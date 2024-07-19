from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Artista, Usuario, Rol, Evento, Noticia, Producto, Carrito, CarritoProducto
from .forms import ProductoForm

# VISTAS PRINCIPALES DE LA PAGINA
def paginicio(request):
    es_admin = False
    if request.user.is_authenticated: # Verifica si el usuario autenticado es administrador
        es_admin = es_admin_funcion(request)
    eventos = Evento.objects.order_by('?').first() # Selecciona un evento aleatorio de la base de datos
    noticia = Noticia.objects.order_by('?').first() # Selecciona una noticia aleatoria de la base de datos
    contexto = {"es_admin": es_admin, 'eventos':eventos,'noticia':noticia}
    return render(request, 'rsound/Index.html', contexto) # Renderiza la plantilla Index.html con el contexto proporcionado

def nosotros(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    contexto = {"es_admin": es_admin}
    return render(request, 'rsound/Nosotros.html', contexto)

def mercancia(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    contexto = {"es_admin": es_admin}
    return render(request, 'rsound/Mercancia.html', contexto)

def novedades(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    contexto = {"es_admin": es_admin}
    return render(request, 'rsound/Novedades.html', contexto)

def registro(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    contexto = {"es_admin": es_admin}
    return render(request, 'rsound/registro.html', contexto)

def evento(request, id_evento):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    evento = Evento.objects.get(idEvento = id_evento)
    contexto = {"es_admin": es_admin,
                "evento": evento}
    return render(request, 'rsound/evento.html', contexto)

def eventos(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    eventos = Evento.objects.all()
    contexto = {"es_admin": es_admin, 'eventos':eventos}
    return render(request, 'rsound/Eventos.html', contexto)

def noticia(request, id_noticia):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    noticia = get_object_or_404(Noticia, idNoticia=id_noticia)
    contexto = {"es_admin": es_admin,"noticia": noticia}
    return render(request, 'rsound/noticia.html', contexto)

def noticias(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    noticia = Noticia.objects.all()
    contexto = {"es_admin": es_admin, 'noticias': noticia}
    return render(request, 'rsound/Noticias.html', contexto)

def artista(request, id_artista):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    artista = Artista.objects.get(idArtista=id_artista)
    contexto = {"es_admin": es_admin, "artista": artista}
    print (id_artista)
    return render(request, 'rsound/artista.html', contexto)
   
def listadoartistas(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
    artistas = Artista.objects.all()
    contexto = {"es_admin": es_admin, 'artistas': artistas}
    return render(request, 'rsound/listadoArtistas.html', contexto)

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

def recuperar_contrasena(request):
    return render(request, 'rsound/recuperar_contrasena.html')

# Vistas de administración
def administracion(request):
    return render(request, 'rsound/Admin/administracion.html')

def adminartistas(request):
    return render(request, 'rsound/Admin/adminArtistas.html')

def adminusuario(request):
    return render(request, 'rsound/Admin/adminUsuario.html')

def adminevento(request):
    return render(request, 'rsound/Admin/adminEvento.html')

def adminnoticia(request):
    return render(request, 'rsound/Admin/adminNoticia.html')

def crear_artista(request):
    return render(request, 'rsound/Admin/crear_artista.html')

def listado_artista(request):
    artista = Artista.objects.all()
    contexto = {"arte": artista}
    return render(request, 'rsound/Admin/listado_artista.html', contexto)

def listado_usuario(request):
    roles = Rol.objects.all()
    usuario = Usuario.objects.all()
    contexto = {"roles": roles, "persona": usuario}
    return render(request, 'rsound/Admin/listado_usuario.html', contexto)

def crear_usuario(request):
    roles = Rol.objects.all()
    contexto = {"roles": roles}
    return render(request, 'rsound/Admin/crear_usuario.html', contexto)

def crear_evento(request):
    roles = Rol.objects.all()
    contexto = {"roles": roles}
    return render(request, 'rsound/Admin/crear_usuario.html', contexto)

def pagEditar_usuario(request, id_usuario):
    usuarioAEditar = Usuario.objects.get(idUsuario=id_usuario)
    roles = Rol.objects.all()
    contexto = {"id_usuario": id_usuario, "usuario": usuarioAEditar, "roles": roles}
    return render(request, 'rsound/Admin/editar_usuario.html', contexto)

# FUNCIONES DE AUTENTICACION
def logout_view(request):
    logout(request) # Cierra la sesión del usuario actual
    return redirect('inicio')  # Redirige al usuario a la página de inicio

def iniciar_sesion(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario POST enviados por el usuario
        usuario1 = request.POST.get('usuario', '')
        contra1 = request.POST.get('contra', '')

# Verifica si los campos de usuario y contraseña están vacíos
        if not usuario1 or not contra1:
            messages.error(request, 'Por favor, ingrese todos los campos.')
            return redirect('inicio')
        
# Intenta obtener el usuario del modelo User de Django
        try:
            user1 = User.objects.get(username=usuario1)
        except User.DoesNotExist:
            messages.error(request, 'El usuario o la contraseña son incorrectas.')   # Si el usuario no existe, muestra un mensaje de error
            return redirect('inicio')
        
# Verifica si la contraseña proporcionada es correcta
        pass_valida = check_password(contra1, user1.password)
        if not pass_valida:
            messages.error(request, 'El usuario o la contraseña son incorrectas.')
            return redirect('inicio')
        
# Obtiene el usuario del modelo personalizado Usuario
        usuario2 = get_object_or_404(Usuario, correo=usuario1)
        user = authenticate(username=usuario1, password=contra1)

        if user is not None:
            login(request, user)
            if usuario2.rol.nombreRol == "Admin":
                usuario2.is_staff = True # Asigna permisos de administrador si es Admin
                usuario2.save()
                return redirect('administracion')
            else:
                usuario2.is_staff = False # No asigna permisos de administrador
                usuario2.save()
                return redirect('inicio')
        else:
            messages.error(request, 'El usuario o la contraseña son incorrectas.')  # Si la autenticación falla, muestra un mensaje de error
            return redirect('inicio')
    return render(request, 'rsound/login.html')



def registrar_usuario(request):
    # Obtiene los datos del formulario POST enviados por el usuario.
    nombreUsu = request.POST['nickname']
    nombres = request.POST['name']
    apellido = request.POST['apellido']
    correoU = request.POST['email']
    claveU = request.POST['password']
    telefonoU = request.POST['telefono']
    # Obtiene el objeto Rol correspondiente al rol de "Usuario".
    rol = Rol.objects.get(nombreRol="Usuario")

# Crea un nuevo objeto Usuario con los datos proporcionados y lo guarda en la base de datos.
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
# Crea un nuevo objeto User para el sistema de autenticación de Django.
    user = User.objects.create_user(
        username=correoU,
        email=correoU,
        password=claveU
    )
    user.first_name = nombreUsu
    user.last_name = apellido
    user.is_staff = False
    user.save()
# Redirige al usuario a la página de inicio después de registrarse.
    return redirect('inicio')

def registrar_usuario_admin(request):
    nombreUsu = request.POST['nickname']
    nombres = request.POST['name']
    apellido = request.POST['apellido']
    correoU = request.POST['email']
    claveU = request.POST['password']
    telefonoU = request.POST['telefono']
    rol = request.POST['rol']
 # Obtiene el objeto Rol basado en el idRol.
    rolModels = Rol.objects.get(idRol=rol)

 #Crea un nuevo objeto Usuario con los datos proporcionados y lo guarda en la base de datos.
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

# Crea un nuevo objeto User para el sistema de autenticación de Django.
    user = User.objects.create_user(
        username=correoU,
        email=correoU,
        password=claveU
    )
    user.first_name = nombreUsu
    user.last_name = apellido
    user.is_staff = False
    if rol == 2:
        user.is_staff = True
    user.save()
    
# Redirige al administrador a la página de administración de usuarios.
    return redirect('adminusuario')

# FUNCIONES DE ARTISTA
def registrar_artista(request):
    nombreArt = request.POST['nameartista']
    image = request.FILES.get('imagen', None)
    biografia = request.POST['biografia']
    discografia = request.POST['discos']
    recopilatorio = request.POST.get('recopilatorio', None)
    videos = request.POST['video']

    Artista.objects.create(
        nombreArtista=nombreArt,
        imagen=image,
        biografiaArtista=biografia,
        discografiaArtista=discografia,
        recopilatorioArtista=recopilatorio,
        video=videos
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

# Funciones para usuarios
def editar_usuario_funcion(request, id_usuario):
    try:
        nombre = request.POST['name']
        apellido = request.POST['apellido']
        nombreusuario = request.POST['nickname']
        emails = request.POST['email']
        telefonos = request.POST['telefono']
        contrasena = request.POST.get('password', None)
        rol = request.POST['rol']

        # EDITAR TABLA USUARIOS
        usuarios = Usuario.objects.get(idUsuario=id_usuario)
        usuarios.nombreUsuario = nombreusuario
        usuarios.apellidos = apellido
        usuarios.nombre = nombre
        usuarios.correo = emails
        usuarios.numero_telefonico = telefonos
        if contrasena:
            usuarios.contraseña = contrasena
        usuarios.rol = Rol.objects.get(idRol=rol)
        usuarios.save()

        # EDITAR TABLA USERS
        userDjango = User.objects.get(username=emails)
        userDjango.email = emails
        userDjango.username = emails
        userDjango.first_name = nombreusuario
        userDjango.last_name = apellido

        # VALIDAR STAFF
        userDjango.is_staff = False
        if rol == 2:
            userDjango.is_staff = True

        userDjango.save()
        messages.success(request, 'Editado Correctamente.')

    except Exception as e:
        messages.error(request, 'Ocurrio un Error.')

    return redirect('listado_usuario')

def eliminar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(idUsuario=id_usuario)
    userDjango = User.objects.get(username=usuario.correo)
    userDjango.delete()
    usuario.delete()
    return redirect('listado_usuario')

# Funciones para eventos
def registrar_evento(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        imagen = request.FILES.get('imagen', None)
        descripcion = request.POST['descripcion']
        video_presentacion = request.POST['video_presentacion']

        Evento.objects.create(
            titulo=titulo,
            imagen=imagen,
            descripcion=descripcion,
            video_presentacion=video_presentacion
        )
        return redirect('adminevento')
    return render(request, 'rsound/Admin/crear_evento.html')

def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('adminevento')
    return render(request, 'rsound/Admin/eliminar_evento.html', {'evento': evento})

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.titulo = request.POST['titulo']
        if 'imagen' in request.FILES:
            evento.imagen = request.FILES['imagen']
        evento.descripcion = request.POST['descripcion']
        evento.video_presentacion = request.POST['video_presentacion']
        evento.save()
        return redirect('adminevento')
    return render(request, 'rsound/Admin/editar_evento.html', {'evento': evento})

def listado_evento(request):
    eventos = Evento.objects.all()
    contexto = {"eventos": eventos}
    return render(request, 'rsound/Admin/listado_evento.html', contexto)

# Funciones para noticias
def registrar_noticia(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        fecha = request.POST['fecha']
        imagen = request.FILES.get('imagen', None)
        descripcion = request.POST['descripcion']
        video_presentacion = request.POST['video_presentacion']

        Noticia.objects.create(
            titulo=titulo,
            fecha=fecha,
            imagen=imagen,
            descripcion=descripcion,
            video_presentacion=video_presentacion
        )
        return redirect('adminnoticia')
    return render(request, 'rsound/Admin/crear_noticia.html')

def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('adminnoticia')
    return render(request, 'rsound/Admin/eliminar_noticia.html', {'noticia': noticia})

def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.titulo = request.POST['titulo']
        noticia.fecha = request.POST['fecha']
        if 'imagen' in request.FILES:
            noticia.imagen = request.FILES['imagen']
        noticia.descripcion = request.POST['descripcion']
        noticia.video_presentacion = request.POST['video_presentacion']
        noticia.save()
        return redirect('adminnoticia')
    return render(request, 'rsound/Admin/editar_noticia.html', {'noticia': noticia})

def listado_noticia(request):
    noticias = Noticia.objects.all()
    contexto = {"noticias": noticias}
    return render(request, 'rsound/Admin/listado_noticia.html', contexto)


# Funciones para producto 

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminproductos')
    else:
        form = ProductoForm()
    return render(request, 'rsound/Admin/crear_producto.html', {'form': form})

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, idProducto=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('adminproductos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'rsound/Admin/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, idProducto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('adminproductos')
    return render(request, 'rsound/Admin/eliminar_producto.html', {'producto': producto})

def adminproductos(request):
    productos = Producto.objects.all()
    return render(request, 'rsound/Admin/adminProductos.html', {'productos': productos})

# Función extra para verificar si el usuario es administrador
def es_admin_funcion(request):
# Obtiene el objeto de usuario desde el request.
    user = request.user
# Obtiene el nombre de usuario del usuario autenticado.
    username = user.username
    usuarioModel = Usuario.objects.get(correo=username)
    rolModel = usuarioModel.rol
 # Devuelve True si el nombre del rol es 'Admin', de lo contrario, devuelve False.
    return rolModel.nombreRol == 'Admin'

#CARRO DE COMPRA Y PRODUCTOS

User = get_user_model()

# Vista para mostrar la página de mercancía
def mercancia(request):
    es_admin = False
    if request.user.is_authenticated:
        es_admin = es_admin_funcion(request)
 # Obtiene todos los productos de la base de datos
    productos = Producto.objects.all()
    contexto = {"es_admin": es_admin, "productos": productos}
    return render(request, 'rsound/Mercancia.html', contexto)
  # Obtiene todos los productos y los pasa al contexto para ser renderizados en la plantilla.


# Esta función permite a los usuarios agregar productos a su carrito.
def agregar_al_carrito(request, producto_id):
    usuario = get_object_or_404(Usuario, correo=request.user.email)
    carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    producto = get_object_or_404(Producto, idProducto=producto_id)
    carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_producto.cantidad += 1
    carrito_producto.save()
    messages.success(request, f'{producto.nombre_producto} se ha añadido al carrito.')
    return redirect('carrito')

# Esta función renderiza la página del carrito de compras.
# Calcula el total del precio de los productos en el carrito.
def carrito(request):
    if request.user.is_authenticated:
        usuario = get_object_or_404(Usuario, correo=request.user.email)
        carrito = get_object_or_404(Carrito, usuario=usuario)
        productos_carrito = CarritoProducto.objects.filter(carrito=carrito)
        total = sum(item.producto.precio * item.cantidad for item in productos_carrito)
        contexto = {"productos_carrito": productos_carrito, "total": total}
    else:
        contexto ={"productos_carrito": "", "total": 0}
    return render(request, 'rsound/Carrito.html', contexto)

# Esta función permite a los usuarios eliminar productos de su carrito.
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(CarritoProducto, id=item_id)
    item.delete()
    messages.success(request, f'{item.producto.nombre_producto} se ha eliminado del carrito.')
    return redirect('carrito')

 # Esta función gestiona el proceso de pago.
 # Obtiene el carrito del usuario y calcula el total.
def pagar(request):
    usuario = get_object_or_404(Usuario, correo=request.user.email)
    carrito = get_object_or_404(Carrito, usuario=usuario)
    productos_carrito = CarritoProducto.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in productos_carrito)
    if request.method == 'POST':
        # Procesar pago aquí
        carrito.productos.clear()
        messages.success(request, 'Compra realizada con éxito.')
        return redirect('inicio')
    contexto = {"productos_carrito": productos_carrito, "total": total}
    return render(request, 'rsound/Pagar.html', contexto)


# BUSCAR
#SOLO BUSCA LOS ARTISTAS NADA MAS
def buscar_artistas(request):
     # Obtiene la consulta de búsqueda del parámetro 'q' de la URL
    query = request.GET.get('q', '')
     # Filtra los artistas cuyo nombre contenga la consulta de búsqueda
    resultados = Artista.objects.filter(nombreArtista__icontains=query)
     # Prepara el contexto con los resultados de la búsqueda y la consulta original
    contexto = {
        'resultados': resultados,
        'query': query
    }
    return render(request, 'rsound/buscar_resultados.html', contexto)