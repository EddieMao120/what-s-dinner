from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient, through="RecipeIngredient", related_name="recipes"
    )

    def __str__(self):
        return self.name

    def can_make_with(self, available_ingredients):
        """Return True if all recipe ingredients are in available_ingredients set."""
        required = {ri.ingredient.name for ri in self.recipeingredient_set.all()}
        return required.issubset(available_ingredients)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = ("recipe", "ingredient")

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} for {self.recipe.name}"
