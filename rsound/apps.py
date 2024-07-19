from django.apps import AppConfig

# Configuración de la aplicación 'rsound'
class RsoundConfig(AppConfig):
     # Define el tipo de campo automático predeterminado para los modelos en esta aplicación
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rsound'
    # Nombre de la aplicación