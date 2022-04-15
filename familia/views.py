from django.shortcuts import render
from .models import Familia

def familia(request):
    familia = Familia(nombre='Pepe', parentesco='Padre', edad='40', fechaDeNacimiento='1950-05-22')
    familia.save()
    return render(request, 'familia/familia.html', {'familia':familia})
