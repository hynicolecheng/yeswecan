import csv
import re
from django.db import models
from django.forms import JSONField
# Create your models here.
class Recipe(models.Model):
    def __str__(self):
        return self.recipe_name
    recipe_name = models.CharField(max_length=200)
    ingredients = models.JSONField()
    recipe_URL = models.CharField(max_length=400)

    def update_recipes():
        with open('../webscraped_data/Recipes_1000.csv', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                name = row[0]
                p = re.findall(r"'(.*?)'",row[1])
                ingr = {ing: 47 for ing in p}
                url = row[2]
                Recipe.objects.create(recipe_name=name, ingredients=ingr, recipe_URL=url)



    #recipe_ingredient_list = QuerySet()
    #recipe.ingredient_set

class Fridge(models.Model):
    def __str__(self):
        return self.fridge_name

    staged_ingr = models.CharField(max_length=200)
    staged_amt = models.IntegerField()
    ingredients = models.JSONField() #ingredients[key]=value to set, ingredients[pop] to get

   #fridge_ingredient_list = QuerySet()
    fridge_name = models.CharField(max_length=200)
   #fridge.ingredient_set
    def get_available_recipes(self):
        rv = []
        for r in Recipe.objects.all():
            if len(set(r.ingredients.keys())) == len(set((r.ingredients.keys())).intersection(set(self.ingredients.keys()))):
                rv.append(r.recipe_URL)

        return rv
        #rv = []
        #create empty list
        #iterate through Recipe.objects.all()
        #for r in Recipe.objects.all():
        #    print(r.ingredient_set)
            #if len(r.ingredient_set) == len((r.ingredient_set).intersection(self.ingredient_set)):
        #    if len(r.ingredient_set.all()) == len((r.ingredient_set.all()).intersection(self.ingredient_set.all())):
        #        rv.append(r.recipe_URL)
        #within each iteration, check if the intersection of recipe's ingredients and fridge's ingredients are of equal size. if so, add to initial list.
        #return list.
        #return rv


#class Ingredient(models.Model):
#    def __str__(self):
#        return self.name
#    name = models.CharField(max_length=200)
#    recipes = models.ManyToManyField(Recipe) 
#    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, default='')
#    def equals(self, other):
#        return (other.name).equals(self.name)
#    #ingredient.recipe_set
#    #ingredient.fridge