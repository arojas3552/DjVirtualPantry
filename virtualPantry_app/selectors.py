#for pulling data rq of recipe recommendations
#business logic

from .models import FoodList, Product, RecipeIndex, Ingredients,RecipeDescription

def recommendRecipe(list_id):
    foodList = FoodList.objects.filter(food_list_id=FoodList.kwargs(list_id))._meta.get_field("title")
    
    recipeList = RecipeDescription.objects.filter(recipe_list_id=1)._meta.get_field("recipeName")

    matchingNames = foodList.intersection(recipeList)

    return matchingNames