from django.shortcuts import render
from experiencia.models import Experiencia

# Create your views here.

def experiencia(request):

    experiencias = Experiencia.objects.all()
    
    return render(request, 'experiencia/experiencia.html', {"experiencias": experiencias})