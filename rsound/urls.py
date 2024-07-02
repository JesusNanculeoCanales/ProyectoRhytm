from .views import paginicio, nosotros,listadoartistas,cerati,mercancia,novedades,registro
from django.urls import path,include

urlpatterns = [
    path('',paginicio,name='inicio'),
    path('nosotros',nosotros,name='nosotros'),
    path('listadoartistas',listadoartistas,name='listadoartistas'),
    path('cerati',cerati,name='cerati'),
    path('mercancia',mercancia,name='mercancia'),
    path('novedades',novedades,name='novedades'),
    path('registro',registro,name='registro'),



    ##funciones
]
