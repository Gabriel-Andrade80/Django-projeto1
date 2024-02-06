from django.shortcuts import render #ler e renderizar arquivo



# Create your views here.


def home(request):
    """funçao para pagina home"""

    return render(request, 'recipes/pages/home.html',context={
        'name': 'Gabriel Andrade',
    } )


def recipe(request,id):
    """funçao para pagina recipe"""

    return render(request, 'recipes/pages/recipe-view.html',context={
        'name': 'Gabriel Andrade',
    })
