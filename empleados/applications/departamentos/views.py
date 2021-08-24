from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from applications.personas.models import *
from .models import *
from .forms import NewDepartamentoForm

# Create your views here.

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamentos/lista.html"
    context_object_name = 'departamentos'


class NewDepartamento(FormView):
    template_name = 'departamentos/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('*****Estamos en el form valid******')

        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job = '1',
            departamento = depa
        )
        return super(NewDepartamento , self).form_valid(form)