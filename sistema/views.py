from django.shortcuts import render
from .models import Obra

def lista_obras(request):
    obras = Obra.objects.all().prefetch_related('genres')
    return render(request, 'catalogo.html', {'obras': obras})


