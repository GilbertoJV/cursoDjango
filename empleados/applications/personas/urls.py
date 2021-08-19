from django.urls import path
from . import views

urlpatterns = [
    path('api/getAllEmpleados/', views.ListAllEmpleados.as_view()),
    path('api/listByArea/<short_name>', views.ListByAreaEmpleado.as_view()),
    #path('api/listByArea/<var_job>', views.ListByTrabajoEmpleado.as_view()),
    path('buscar_empleado/', views.ListEmpleadoByKword.as_view()),
    path('habilidades_empleado/', views.ListHabilidadesEmpleado.as_view()),
]
