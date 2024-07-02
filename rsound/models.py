from django.db import models

# Create your models here.
class Rol(models.Model):
    idRol = models.AutoField(primary_key=True,verbose_name='Id rol')         
    nombreRol = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self) -> str:
        return str(self.idRol)+" "+self.nombreRol

class Usuario(models.Model):
    idUsuario =models.AutoField(primary_key=True,verbose_name='Id usuario')
    nombreUsuario =models.CharField(max_length=15, null=False)
    nombre = models.CharField(max_length=20, null=False)
    apellidos= models.CharField(max_length=40, null=False)
    numero= models.IntegerField()
    correo=models.CharField(max_length=40, null=False)
    contraseña=models.CharField(max_length=20, null=False)
    fechacreacion =models.DateField(verbose_name='Fecha creacion')
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.idUsuario)+" "+self.nombreUsuario