#for pulling data rq of recipe recommendations
#business logic

from .models import Product, Ingredients
from django.db.models.functions import Lower



def recommendRecipe(list_id):
    #foodList = FoodList.objects.filter(FoodList(list_id))._meta.get_field("title")
    #recipeList = RecipeDescription.objects.filter(recipe_list_id=1)._meta.get_field("recipeName")
    
    #matchingNames = (FoodList.objects.filter(FoodList(list_id))._meta.get_field("title")).intersection((RecipeDescription.objects.filter(recipe_list_id=1)._meta.get_field("recipeName"))))
    #recipeList.objects.filter()
    
    allIngredients = set(Ingredients.objects.values_list('ingredientName',flat=True))
    myIngredients = set(Product.objects.values_list('productName',flat=True))
    #allIngredients = Ingredients.objects.annotate(ingredient_lower=Lower('ingredientName'))
    #myIngredients = Product.objects.annotate(ingredient_lower=Lower('productName'))
    #allIngredients = set(allIngredients)
    #myIngredients = set(myIngredients)
    

    #DEBUG
    print("Entire recipe list\t")
    print(Ingredients.objects.values_list('ingredientName',flat=True))
    print(allIngredients)
    print("My food list\t")
    print(Product.objects.values_list('productName',flat=True))
    print(myIngredients)
    print("Matching names\t")

    matchingNames = allIngredients.intersection(myIngredients)
    print(matchingNames)
    objMatching =[]

    for ingredient in matchingNames:
        objMatching.append(Ingredients.objects.get(ingredientName = ingredient).ingredientList_id)

    return objMatching
