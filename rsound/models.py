from django.db import models
from django.contrib.auth.hashers import make_password

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True,verbose_name='Id rol')         
    nombreRol = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self) -> str:
        return str(self.idRol)+" "+self.nombreRol
    
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='Id de usuario')
    nombreUsuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    numero_telefonico = models.CharField(max_length=20, verbose_name="Número Telefónico (+56)", default='0000000000')
    correo = models.EmailField(max_length=40)
    contraseña = models.CharField(max_length=128)  
    fechacreacion = models.DateField(verbose_name='Fecha de creación', auto_now_add=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.contraseña = make_password(self.contraseña)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.idUsuario} {self.nombreUsuario}"

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
    
class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True, verbose_name='Id de Evento')
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='eventos/')
    descripcion = models.TextField()
    video_presentacion = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='favoritos')
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='favoritos')

    def __str__(self):
        return f"Favorito de {self.usuario.nombreUsuario} - {self.artista.nombreArtista}"

    


    