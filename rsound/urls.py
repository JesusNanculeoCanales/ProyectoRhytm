from django.urls import path
from .views import (
    artista,noticias,eventos,adminnoticia,eliminar_noticia,editar_noticia,registrar_noticia,listado_noticia,adminnoticia,listado_evento,eliminar_evento,editar_evento,registrar_evento,iniciar_sesion,editar_usuario_funcion,registrar_usuario_admin,pagEditar_usuario, paginicio, nosotros, listadoartistas, crear_artista, mercancia, novedades, registro, 
    evento, noticia, aespa, smiths, jungkook, blur, newjeans, cerati, logout_view, 
    registrar_usuario, administracion, adminartistas, adminusuario, crear_usuario, listado_usuario, 
    registrar_artista, crear_artista, listado_artista, editar_artista, eliminar_artista, eliminar_usuario, editar_usuario_funcion,adminevento,adminproductos,crear_producto,editar_producto,eliminar_producto,
    agregar_al_carrito,carrito,eliminar_del_carrito,pagar
)

urlpatterns = [

    # HTML VISTA USUARIO
    path('', paginicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('artista/<id_artista>', artista, name='artista'),
    path('listadoartistas/', listadoartistas, name='listadoartistas'),
    path('mercancia/', mercancia, name='mercancia'),
    path('novedades/', novedades, name='novedades'),
    path('evento/<id_evento>', evento, name='evento'),
    path('eventos/',eventos, name='eventos'),
    path('noticia/<id_noticia>', noticia, name='noticia'),
    path('noticias/',noticias, name='noticias'),
    path('cerati/', cerati, name='cerati'),
    path('smiths/', smiths, name='smiths'),
    path('jungkook/', jungkook, name='jungkook'),
    path('blur/', blur, name='blur'),
    path('newjeans/', newjeans, name='newjeans'),
    path('aespa/', aespa, name='aespa'),
    path('registro/', registro, name='registro'),
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    
    #ADMIN usuario.
    path('registrar_usuario_admin/',registrar_usuario_admin, name='registrar_usuario_admin'),
    path('pagEditar_usuario/<id_usuario>', pagEditar_usuario, name='pagEditar_usuario'),
    path('editar_usuario_funcion/<id_usuario>', editar_usuario_funcion, name='editar_usuario_funcion'),
    path('eliminar_usuario/<id_usuario>', eliminar_usuario, name='eliminar_usuario'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('listado_usuario/', listado_usuario, name='listado_usuario'),

    #ADMIN vistas administrador.
    path('administracion/', administracion, name='administracion'),
    path('adminartistas/', adminartistas, name='adminartistas'),
    path('adminusuario/', adminusuario, name='adminusuario'),
    path('adminevento/', adminevento, name='adminevento'),
    path('adminnoticia/', adminnoticia, name='adminnoticia'),

    #ADMIN artistas.
    path('crear_artista/', crear_artista, name='crear_artista'),
    path('registrar_artista/', registrar_artista, name='registrar_artista'),
    path('listado_artista/', listado_artista, name='listado_artista'),
    path('artista/editar/<int:pk>/', editar_artista, name='editar_artista'),
    path('artista/eliminar/<int:pk>/', eliminar_artista, name='eliminar_artista'),

    #ADMIN eventos.
    path('evento/crear/', registrar_evento, name='crear_evento'),
    path('evento/editar/<int:pk>/', editar_evento, name='editar_evento'),
    path('evento/eliminar/<int:pk>/', eliminar_evento, name='eliminar_evento'),
    path('listado_evento/', listado_evento, name='listado_evento'),

    #ADMIN noticia.
    path('listado_noticia/', listado_noticia, name='listado_noticia'),
    path('noticia/crear/', registrar_noticia, name='crear_noticia'),
    path('noticia/editar/<int:pk>/', editar_noticia, name='editar_noticia'),
    path('noticia/eliminar/<int:pk>/', eliminar_noticia, name='eliminar_noticia'),

    #ADMIN producto.
    path('adminproductos/', adminproductos, name='adminproductos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:id_producto>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id_producto>/', eliminar_producto, name='eliminar_producto'),

    #INICIO SESION
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
    path('logout/', logout_view, name='logout'),

    #
    path('agregar_al_carrito/<int:producto_id>/',agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/',carrito, name='carrito'),
    path('eliminar_del_carrito/<int:item_id>/',eliminar_del_carrito, name='eliminar_del_carrito'),
    path('pagar/',pagar, name='pagar'),

]











