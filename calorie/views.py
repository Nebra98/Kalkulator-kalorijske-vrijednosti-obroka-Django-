from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Kategorija, Jelo

# Create your views here.

def index(request):
    lista_kategorija = Kategorija.objects.order_by('pub_date')
    lista_jela = Jelo.objects.order_by('-naziv_jela')
    context = {
        'lista_kategorija': lista_kategorija,
        'lista_jela': lista_jela,
        'brojac': 0,
    }
    return render(request, 'calorie/index.html', context)
