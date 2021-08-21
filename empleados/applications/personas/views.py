from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "personas/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'

        return context

class SuccessView(TemplateView):
    template_name = 'personas/success.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'personas/add.html'
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('personas_app:correcto')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'personas/update.html'
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('personas_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request, *args, **kwargs)

class EmpleadoDeleteView(DeleteView):
    model =  Empleado
    template_name = 'personas/delete.html'
    success_url = reverse_lazy('personas_app:correcto')
    

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