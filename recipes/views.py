from django.shortcuts import render #ler e renderizar arquivo
from utils.recipes.factory import make_recipe


# Create your views here.


def home(request):
    """funçao para pagina home"""

    return render(request, 'recipes/pages/home.html',context={
        'recipes': [make_recipe() for _ in range(10)],
    } )


def recipe(request,id):
    """funçao para pagina recipe"""

    return render(request, 'recipes/pages/recipe-view.html',context={
        'recipe': make_recipe(),
    })
