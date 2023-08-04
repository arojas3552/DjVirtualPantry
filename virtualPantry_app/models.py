from django.utils import timezone
from django.db import models
from django.urls import reverse


#function returns time in one week for default expiration of fruit and veggies
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7) #in one week...

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class FoodList(models.Model):
    title = models.CharField(max_length=100, unique=True)
   # slug=models.SlugField(max_length=250)

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
    category = models.CharField(max_length=1, choices=PRODUCT_CATEGORIES)
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