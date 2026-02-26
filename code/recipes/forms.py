from django import forms
from .models import Ingredient


class IngredientSelectionForm(forms.Form):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.order_by("name"),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select ingredients you have on hand",
    )
