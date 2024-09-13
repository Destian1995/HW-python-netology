from django.shortcuts import render
from django.http import HttpResponseBadRequest

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def index(request):
    """Отображение списка доступных рецептов на главной странице."""
    context = {'recipes': DATA.keys()}
    return render(request, 'calculator/index.html', context)


def recipe_view(request, dish):
    """Отображение конкретного рецепта."""
    recipe = DATA.get(dish)
    if recipe is None:
        return HttpResponseBadRequest("Такого рецепта не знаю :(")

    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
    except ValueError:
        return HttpResponseBadRequest("Некорректное значение для servings")

    # Умножаем ингредиенты на количество порций
    recipe_servings = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': recipe_servings
    }
    return render(request, 'calculator/recipe.html', context)
