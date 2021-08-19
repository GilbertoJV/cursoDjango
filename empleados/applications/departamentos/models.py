from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=50)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Departamentos de la empresa'
        verbose_name_plural = 'Todos los departamentos'
        ordering = ['name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.short_name