from django.contrib import admin

from .models import Recipe, Fridge

#class IngredientInline(admin.TabularInline):
#    model = Ingredient
 #   extras = 1

class FridgeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['fridge_name', 'ingredients']})
    ]
    #inlines = [IngredientInline]
admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Recipe)
#admin.site.register(Ingredient)