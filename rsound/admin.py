from django.contrib import admin
from .models import Rol,Usuario,Artista,Evento,Favorito,Noticia,Producto

# Registra los modelos para que puedan ser administrados a través del sitio de administración de Django.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Artista)
admin.site.register(Evento)
admin.site.register(Favorito)
admin.site.register(Noticia)
admin.site.register(Producto)

