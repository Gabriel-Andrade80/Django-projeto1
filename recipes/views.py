from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    """funçao para pagina home"""

    return HttpResponse('HOME 1')


def contato(request):
    """funçao para pagina contato"""

    return HttpResponse('contato 2')


def sobre(request):
    """funçao para pagina sobre"""

    return HttpResponse('sobre 3')
