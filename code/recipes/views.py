from django.shortcuts import render

from .forms import IngredientSelectionForm
from .models import Recipe


# Create your views here.

def index(request):
    form = IngredientSelectionForm(request.GET or None)
    recipes = None
    if form.is_valid():
        selected = {ing.name for ing in form.cleaned_data['ingredients']}
        # fetch all recipes and filter
        recipes = []
        for recipe in Recipe.objects.prefetch_related('recipeingredient_set__ingredient'):
            if recipe.can_make_with(selected):
                recipes.append(recipe)
    return render(request, 'recipes/index.html', {'form': form, 'recipes': recipes})
