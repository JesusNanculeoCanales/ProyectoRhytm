from django.db import models
from django.contrib.auth.hashers import make_password

# Define los diferentes roles que un usuario puede tener.
class Rol(models.Model):
    idRol = models.AutoField(primary_key=True,verbose_name='Id rol') # Campo de clave primaria           
    nombreRol = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self) -> str:
        return str(self.idRol)+" "+self.nombreRol
    
# Contiene la información de los usuarios registrados en el sistema.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='Id de usuario')
    nombreUsuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    numero_telefonico = models.CharField(max_length=20, verbose_name="Número Telefónico (+56)", default='0000000000')
    correo = models.EmailField(max_length=40)
    contraseña = models.CharField(max_length=128)  
    fechacreacion = models.DateField(verbose_name='Fecha de creación', auto_now_add=True)
    # Relación de clave foránea con la tabla Rol. Define qué rol tiene el usuario.
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

# Método save para guardar la contraseña en formato hash.
    def save(self, *args, **kwargs):
        self.contraseña = make_password(self.contraseña)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.idUsuario} {self.nombreUsuario}" # Devuelve una cadena con el ID y el nombre de usuario.

# Contiene la información de los artistas.
class Artista(models.Model):
    idArtista = models.AutoField(primary_key=True, verbose_name='Id de Artista')
    nombreArtista = models.CharField(max_length=100)
    imagen= models.ImageField(null=True,upload_to="rsound")
    biografiaArtista = models.TextField()
    discografiaArtista = models.TextField()
    recopilatorioArtista = models.TextField()
    video = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.nombreArtista
    
#Contiene la información de los eventos.
class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True, verbose_name='Id de Evento')
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='eventos/')
    descripcion = models.TextField()
    video_presentacion = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    
# Relaciona a los usuarios con sus artistas favoritos.
class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='favoritos')
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='favoritos')

    def __str__(self):
        return f"Favorito de {self.usuario.nombreUsuario} - {self.artista.nombreArtista}"
    
# Contiene la información de las noticias.
class Noticia(models.Model):
    idNoticia = models.AutoField(primary_key=True, verbose_name='Id de Noticia')
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(verbose_name='Fecha de Publicación')
    imagen = models.ImageField(upload_to='noticias/')
    descripcion = models.TextField()
    video_presentacion = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    
# Contiene la información de los productos.   
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='Id de Producto')
    nombre_producto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="productos/")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre_producto

# Relaciona a los usuarios con sus carritos de compra.
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

#Relaciona los productos con los carritos de compra y la cantidad de cada producto.
class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    

    


    