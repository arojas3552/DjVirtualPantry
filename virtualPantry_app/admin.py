from django.contrib import admin
from virtualPantry_app.models import Person,FoodList,Product

# Register your models here.
admin.site.register(Person)
admin.site.register(FoodList)
admin.site.register(Product)