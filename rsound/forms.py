from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'imagen', 'precio', 'artista']

# Este formulario es para manejar los productos. 
    # Al usar forms.ModelForm, Django nos ayuda a crear formularios basados en nuestro modelo Producto automáticamente.
    # Solo necesitamos especificar los campos que queremos usar: 'nombre_producto', 'imagen', 'precio' y 'artista'.

