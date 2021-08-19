from django.urls import path

def DesdeApss(self):
    print('==============DESDE APP DEPARTAMENTO================')

urlpatterns = [
    path('departamento/', DesdeApss),
]
