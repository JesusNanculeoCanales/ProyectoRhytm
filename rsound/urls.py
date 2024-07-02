from .views import paginicio, nosotros,listadoartistas,mercancia,novedades,registro,evento,noticia,aespa,smiths,jungkook,blur,newjeans,cerati
from django.urls import path,include

urlpatterns = [
    path('',paginicio,name='inicio'),
    path('nosotros',nosotros,name='nosotros'),
    path('listadoartistas',listadoartistas,name='listadoartistas'),
    path('mercancia',mercancia,name='mercancia'),
    path('novedades',novedades,name='novedades'),
    path('registro',registro,name='registro'),
    path('evento',evento,name='evento'),
    path('noticia',noticia,name='noticia'),
    path('cerati',cerati,name='cerati'),
    path('smiths',smiths,name='smiths'),
    path('jungkook',jungkook,name='jungkook'),
    path('blur',blur,name='blur'),
    path('newjeans',newjeans,name='newjeans'),
    path('aespa',aespa,name='aespa'),

]
