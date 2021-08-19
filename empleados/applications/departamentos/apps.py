from django.apps import AppConfig


class DepartamentosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.departamentos'


#agreggar el prefijo de 'applications' que es el nombre de la carpeta contenedora de las apps