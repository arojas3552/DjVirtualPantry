from django.contrib import admin
from virtualPantry_app.models import FoodList,Product,RecipeIndex,RecipeDescription,Ingredients

# Register your models here.
admin.site.register(FoodList)
admin.site.register(Product)
admin.site.register(RecipeIndex)
admin.site.register(RecipeDescription)
admin.site.register(Ingredients)