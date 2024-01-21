from django.shortcuts import render #ler e renderizar arquivo
from django.http import HttpResponse


# Create your views here.


def home(request):
    """funçao para pagina home"""

    return render(request, 'recipes/home.html',context={
        'name': 'Gabriel Andrade',
    } )


def contato(request):
    """funçao para pagina contato"""

    return render(request,'temp/temp.html')


def sobre(request):
    """funçao para pagina sobre"""

    return HttpResponse('sobre 3')
