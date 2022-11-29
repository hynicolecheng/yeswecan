from django.db import models

# Create your models here.
class Recipe(models.Model):
    def __str__(self):
        return self.recipe_name
    recipe_name = models.CharField(max_length=200)
    recipe_URL = models.CharField(max_length=400)
    #recipe_ingredient_list = QuerySet()
    #recipe.ingredient_set

class Fridge(models.Model):
    def __str__(self):
        return self.fridge_name
   #fridge_ingredient_list = QuerySet()
    fridge_name = models.CharField(max_length=200)
   #fridge.ingredient_set
    def get_available_recipes(self):
        rv = []
        #create empty list
        #iterate through Recipe.objects.all()
        for r in Recipe.objects.all():
            print(r.ingredient_set)
            #if len(r.ingredient_set) == len((r.ingredient_set).intersection(self.ingredient_set)):
            if len(r.ingredient_set.all()) == len((r.ingredient_set.all()).intersection(self.ingredient_set.all())):
                rv.append(r.recipe_URL)
        #within each iteration, check if the intersection of recipe's ingredients and fridge's ingredients are of equal size. if so, add to initial list.
        #return list.
        return rv


class Ingredient(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe) 
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, default='')
    def equals(self, other):
        return (other.name).equals(self.name)
    #ingredient.recipe_set
    #ingredient.fridge