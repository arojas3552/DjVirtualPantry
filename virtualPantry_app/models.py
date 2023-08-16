from django.utils import timezone
from django.db import models
from django.urls import reverse


#function returns time in one week for default expiration of fruit and veggies
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7) #in one week...


class RecipeIndex(models.Model):
    indexName = models.CharField(max_length=250, unique=True)

    def get_absolute_url(self):
        return reverse("recipe-index", args=[self.id])

    def __str__(self):
        return self.indexName
    
class RecipeDescription(models.Model):
    RECIPE_CATEGORIES = [
        ("b", "Breakfast"),
        ("l", "Lunch"),
        ("d", "Dinner"),
        ("t", "Dessert"),
        ("s", "Snack"),
        ("o", "Other"),
    ]
    recipeName = models.CharField(max_length=250, unique=True)
    recipe_instructions = models.TextField();
    recipe_list = models.ForeignKey(RecipeIndex, on_delete=models.CASCADE)
    recipeCategory = models.CharField(max_length=1, choices=RECIPE_CATEGORIES,default='Other')

    def get_absolute_url(self):
        return reverse("recipe-view", args=[self.id])

    def __str__(self):
        return self.recipeName

class Ingredients(models.Model):
    ingredientName = models.CharField(max_length=200,unique=True)
    ingredientList = models.ForeignKey(RecipeDescription, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredientName
    


class FoodList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title
    

class Product(models.Model):
    PRODUCT_CATEGORIES = [
        ("F", "Fruit"),
        ("V", "Vegetable"),
        ("G", "Grains"),
        ("P", "Protein"),
        ("D", "Dairy"),
        ("O", "Other"),
    ]

    productName = models.CharField(max_length=200,unique=True)
    category = models.CharField(max_length=1, choices=PRODUCT_CATEGORIES, default="Other")
    entry_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField(default=one_week_hence)
    food_list = models.ForeignKey(FoodList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.food_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.productName}"

    
    class Meta:
        ordering = ["expire_date"]