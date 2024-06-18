from .views import paginicio, nosotros,listadoartistas,cerati,registrarse
from django.urls import path,include

urlpatterns = [
    path('',paginicio,name='inicio'),
    path('nosotros',nosotros,name='nosotros'),
    path('listadoartistas',listadoartistas,name='listadoartistas'),
    path('cerati',cerati,name='cerati'),

    ##funciones
    path('registrarse',registrarse,name='registrarse')
]
