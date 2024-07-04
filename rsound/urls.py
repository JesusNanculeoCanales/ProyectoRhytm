from django.urls import path
from .views import paginicio, nosotros, listadoartistas, crear_artista, editar_artista, eliminar_artista, mercancia, novedades, registro, evento, noticia, aespa, smiths, jungkook, blur, newjeans, cerati, login_view, logout_view,registrar_usuario,administracion,adminartistas,adminusuario,crear_usuario,listado_usuario

urlpatterns = [
    path('', paginicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('listadoartistas/', listadoartistas, name='listadoartistas'),
    path('administracion/',administracion, name='administracion'),
    path('mercancia/', mercancia, name='mercancia'),
    path('novedades/', novedades, name='novedades'),
    path('registro/', registro, name='registro'),
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    path('evento/', evento, name='evento'),
    path('noticia/', noticia, name='noticia'),
    path('cerati/', cerati, name='cerati'),
    path('smiths/', smiths, name='smiths'),
    path('jungkook/', jungkook, name='jungkook'),
    path('blur/', blur, name='blur'),
    path('newjeans/', newjeans, name='newjeans'),
    path('aespa/', aespa, name='aespa'),
    path('artista/crear/', crear_artista, name='crear_artista'),
    path('artista/editar/<int:pk>/', editar_artista, name='editar_artista'),
    path('artista/eliminar/<int:pk>/', eliminar_artista, name='eliminar_artista'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('adminartistas/', adminartistas, name='adminartistas'),
    path('adminusuario/', adminusuario, name='adminusuario'),
    path('crear_usuario/',crear_usuario, name='crear_usuario'),
    path('listado_usuario/',listado_usuario, name='listado_usuario'),
]











