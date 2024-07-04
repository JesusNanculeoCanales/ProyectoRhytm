from django import forms
from .models import Artista, Usuario

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombreArtista', 'biografiaArtista', 'discografiaArtista', 'recopilatorioArtista', 'video']
        widgets = {
            'nombreArtista': forms.TextInput(attrs={'class': 'form-control'}),
            'biografiaArtista': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'discografiaArtista': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'recopilatorioArtista': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'video': forms.URLInput(attrs={'class': 'form-control'})
        }
        labels = {
            'nombreArtista': 'Nombre del Artista',
            'biografiaArtista': 'Biografía',
            'discografiaArtista': 'Discografía',
            'recopilatorioArtista': 'Recopilatorios',
            'video': 'Enlace a Video'
        }
        help_texts = {
            'video': 'Ingrese una URL válida.',
        }
        error_messages = {
            'nombreArtista': {
                'max_length': "Este nombre es demasiado largo.",
                'required': "Este campo es obligatorio."
            },
            'video': {
                'invalid': "Ingrese una URL válida."
            }
        }

class RegistroForm(forms.ModelForm):
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Contraseña")

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'nombreUsuario', 'numero_telefonico', 'correo', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
        labels = {
            'nombre': 'Nombres',
            'apellidos': 'Apellidos',
            'nombreUsuario': 'Nombre de Usuario',
            'numero_telefonico': 'Número Telefónico (+56)',
            'correo': 'Correo Electrónico',
            'contraseña': 'Contraseña',
        }
        help_texts = {
            'correo': 'Ingrese un correo electrónico válido.',
        }
        error_messages = {
            'nombreUsuario': {
                'max_length': "Este nombre es demasiado largo.",
                'required': "Este campo es obligatorio."
            },
            'correo': {
                'invalid': "Ingrese un correo electrónico válido.",
                'required': "Este campo es obligatorio."
            },
            'contraseña': {
                'required': "Este campo es obligatorio."
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get("contraseña")
        confirmar_contraseña = cleaned_data.get("confirmar_contraseña")

        if contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
