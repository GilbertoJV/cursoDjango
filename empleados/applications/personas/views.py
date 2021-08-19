from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'personas/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado

class ListByAreaEmpleado(ListView):
    """ lista empleados de un area """
    template_name = 'personas/list_by_area.html'
    model = Empleado

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista

class ListEmpleadoByKword(ListView):
    """ lista empleado por palabra clave"""
    template_name = 'personas/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'personas/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()

# class ListByTrabajoEmpleado(ListView):
#     """ lista empleados de un area """
#     template_name = 'personas/list_by_trabajo.html'
#     model = Empleado

#     def get_queryset(self):
#         trabajo = self.kwargs['var_job']
#         print(f"-----------------{trabajo}")
#         lista = Empleado.objects.filter(
#             job=trabajo
#         )
#         return lista