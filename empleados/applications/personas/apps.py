from django.apps import AppConfig


class PersonasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.personas'


#agreggar el prefijo de 'applications' que es el nombre de la carpeta contenedora de las apps