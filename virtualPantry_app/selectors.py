#for pulling data rq of recipe recommendations
#business logic

from .models import Product, Ingredients
from django.db.models.functions import Lower



def recommendRecipe():

    #matchingNames = (FoodList.objects.filter(FoodList(list_id))._meta.get_field("title")).intersection((RecipeDescription.objects.filter(recipe_list_id=1)._meta.get_field("recipeName"))))
    #recipeList.objects.filter()
    
    allIngredients = set(Ingredients.objects.values_list('ingredientName',flat=True))
    myIngredients = set(Product.objects.values_list('productName',flat=True))

    matchingNames = allIngredients.intersection(myIngredients)
    print(matchingNames)
    objMatching =[]

    for ingredient in matchingNames:
        objMatching.append(Ingredients.objects.get(ingredientName = ingredient).ingredientList_id)

    return objMatching
