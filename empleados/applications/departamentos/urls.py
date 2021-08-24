from django.urls import path
from . import views

app_name = 'departamentos_app'

urlpatterns = [
    path('departamento_lista/', views.DepartamentoListView.as_view(), name='departamento_list'),
    path('new_departamento/', views.NewDepartamento.as_view(), name='nuevo_departamento'),
]
