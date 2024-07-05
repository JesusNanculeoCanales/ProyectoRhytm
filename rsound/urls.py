from django.urls import path
from .views import (
    listado_evento,eliminar_evento,editar_evento,registrar_evento,iniciar_sesion,editar_usuario_funcion,registrar_usuario_admin,pagEditar_usuario, paginicio, nosotros, listadoartistas, crear_artista, mercancia, novedades, registro, 
    evento, noticia, aespa, smiths, jungkook, blur, newjeans, cerati, logout_view, 
    registrar_usuario, administracion, adminartistas, adminusuario, crear_usuario, listado_usuario, 
    registrar_artista, crear_artista, listado_artista, editar_artista, eliminar_artista, eliminar_usuario, editar_usuario_funcion,adminevento
)

urlpatterns = [

    # HTML VISTA USUARIO

    path('', paginicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('listadoartistas/', listadoartistas, name='listadoartistas'),
    path('mercancia/', mercancia, name='mercancia'),
    path('novedades/', novedades, name='novedades'),
    path('evento/', evento, name='evento'),
    path('noticia/', noticia, name='noticia'),
    path('cerati/', cerati, name='cerati'),
    path('smiths/', smiths, name='smiths'),
    path('jungkook/', jungkook, name='jungkook'),
    path('blur/', blur, name='blur'),
    path('newjeans/', newjeans, name='newjeans'),
    path('aespa/', aespa, name='aespa'),
    path('registro/', registro, name='registro'),
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    
    #ADMIN
    path('registrar_usuario_admin/',registrar_usuario_admin, name='registrar_usuario_admin'),
    path('pagEditar_usuario/<id_usuario>', pagEditar_usuario, name='pagEditar_usuario'),
    path('editar_usuario_funcion/<id_usuario>', editar_usuario_funcion, name='editar_usuario_funcion'),
    path('eliminar_usuario/<id_usuario>', eliminar_usuario, name='eliminar_usuario'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('listado_usuario/', listado_usuario, name='listado_usuario'),


    path('administracion/', administracion, name='administracion'),
    path('adminartistas/', adminartistas, name='adminartistas'),
    path('adminusuario/', adminusuario, name='adminusuario'),
    path('adminevento/', adminevento, name='adminevento'),


    path('crear_artista/', crear_artista, name='crear_artista'),
    path('registrar_artista/', registrar_artista, name='registrar_artista'),
    path('listado_artista/', listado_artista, name='listado_artista'),
    path('artista/editar/<int:pk>/', editar_artista, name='editar_artista'),
    path('artista/eliminar/<int:pk>/', eliminar_artista, name='eliminar_artista'),


    path('evento/crear/', registrar_evento, name='crear_evento'),
    path('evento/editar/<int:pk>/', editar_evento, name='editar_evento'),
    path('evento/eliminar/<int:pk>/', eliminar_evento, name='eliminar_evento'),
    path('listado_evento/', listado_evento, name='listado_evento'),

    #INICIO SESION
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
    path('logout/', logout_view, name='logout'),

 
]











