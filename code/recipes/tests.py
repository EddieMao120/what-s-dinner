from django.test import TestCase
from django.urls import reverse

from .models import Ingredient, Recipe, RecipeIngredient


class RecipeModelTests(TestCase):
    def setUp(self):
        self.i1 = Ingredient.objects.create(name="Tomato")
        self.i2 = Ingredient.objects.create(name="Cheese")
        self.recipe = Recipe.objects.create(name="Tomato Salad", instructions="Mix.")
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.i1)

    def test_can_make_with_available_ingredient(self):
        self.assertTrue(self.recipe.can_make_with({"Tomato"}))
        self.assertFalse(self.recipe.can_make_with({"Cheese"}))


class RecipeViewTests(TestCase):
    def setUp(self):
        # create ingredients & recipe
        self.tomato = Ingredient.objects.create(name="Tomato")
        self.cheese = Ingredient.objects.create(name="Cheese")
        self.soup = Recipe.objects.create(name="Tomato Soup", instructions="Boil.")
        RecipeIngredient.objects.create(recipe=self.soup, ingredient=self.tomato)

    def test_index_lists_matching_recipes(self):
        url = reverse('recipe_index')
        response = self.client.get(url, {'ingredients': [self.tomato.pk]})
        self.assertContains(response, "Tomato Soup")
        # should not list recipe when ingredient not provided
        response2 = self.client.get(url, {'ingredients': [self.cheese.pk]})
        self.assertNotContains(response2, "Tomato Soup")
