from calendar import c
from django import forms
from django.forms import ModelForm
from models import Ingredient, Fridge, Recipe

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        exclude = ['recipes', 'fridge']