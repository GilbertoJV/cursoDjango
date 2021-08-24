from django.urls import path
from . import views

app_name = 'personas_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),


    path('api/getAllEmpleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('api/listByArea/<short_name>', views.ListByAreaEmpleado.as_view()),
    #path('api/listByArea/<var_job>', views.ListByTrabajoEmpleado.as_view()),
    path('buscar_empleado/', views.ListEmpleadoByKword.as_view()),
    path('habilidades_empleado/', views.ListHabilidadesEmpleado.as_view()),
    path('ver_empleado/<pk>', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add_empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update/<pk>', views.EmpleadoUpdateView.as_view(), name='modificar'),
    path('delete/<pk>', views.EmpleadoDeleteView.as_view(), name='eliminar'),
]
