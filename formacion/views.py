from django.shortcuts import render
from formacion.models import Formacion

# Create your views here.
def formacion(request):

    formaciones = Formacion.objects.all()

    return render(request, 'formacion/formacion.html', {"formaciones": formaciones})