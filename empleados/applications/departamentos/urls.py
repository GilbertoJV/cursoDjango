from django.urls import path
from . import views

urlpatterns = [
    path('new_departamento/', views.NewDepartamento.as_view(), name='nuevo_departamento'),
]
