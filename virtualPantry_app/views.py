from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView,CreateView,UpdateView,DeleteView)

from .models import FoodList, Product, RecipeIndex, Ingredients,RecipeDescription

#LIST
class ListListView(ListView):
    model = FoodList
    template_name = "virtualPantry_app/index.html"

class ItemListView(ListView):
    model = Product
    template_name = "virtualPantry_app/virtualPantry_list.html"

    def get_queryset(self):
        return Product.objects.filter(food_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["food_list"] = FoodList.objects.get(id=self.kwargs["list_id"])
        return context
    
#CREATE

class ListCreate(CreateView):
    model = FoodList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = Product
    fields = [
        "food_list",
        "productName",
        "category",
        "expire_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        food_list = FoodList.objects.get(id=self.kwargs["list_id"])
        initial_data["food_list"] = food_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        food_list = FoodList.objects.get(id=self.kwargs["list_id"])
        context["food_list"] = food_list
        context["productName"] = "Add a new food item"
        context["category"] = "Add category"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.food_list_id])

#UPDATE

class ItemUpdate(UpdateView):
    model = Product
    fields = [
        "food_list",
        "productName",
        "expire_date",
    ]

    def get_context_data(self):
        context = super().get_context_data()
        context["food_list"] = self.object.food_list
        context["productName"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.food_list_id])
    

#DELETE

class ListDelete(DeleteView):
    model = FoodList
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food_list"] = self.object.food_list
        return context
    

#RECIPE FEATURE
class RecipeIndexView(ListView):
    model=RecipeDescription
    template_name = "virtualPantry_app/recipe_index.html"

    def get_queryset(self):
        return RecipeDescription.objects.filter(recipeList_id=self.kwargs["index_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["recipe_list"] = RecipeIndex.objects.get(id=self.kwargs["index_id"])
        return context


class RecipeIngredientView(ListView):
    model=Ingredients
    template_name = "virtualPantry_app/recipe_list.html"

    def get_queryset(self):
        return Ingredients.objects.filter(food_list_id=self.kwargs["recipe_id"])
    
    def get_context_data(self):
        context = super().get_context_data()
        context["recipe_description"] = RecipeDescription.objects.get(id=self.kwargs["recipe_id"])
        context["ingredient_list"] = Ingredients.objects.get(id=self.kwargs["recipe_id"])
        return context
    

class RecipeIndexCreate(CreateView):
    model = RecipeIndex
    fields = ["indexName"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["indexName"] = "Add a new recipe Index"
        return context


class IngredientCreate(CreateView):
    model = Ingredients
    fields = [
        "ingredient_list",
        "IngredientName",
        "category",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        ingredient_list = RecipeDescription.objects.get(id=self.kwargs["recipe_id"])
        initial_data["ingredient_list"] = ingredient_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        ingredient_list = RecipeDescription.objects.get(id=self.kwargs["recipe_id"])
        context["ingredient_list"] = ingredient_list
        context["IngredientName"] = "Add a new ingredient"
        context["category"] = "Add category"
        return context

    def get_success_url(self):
        return reverse("recipe-view", args=[self.object.ingredient_list_id])


class RecipeCreate(CreateView):
    model = RecipeDescription
    fields = [
        "recipe_instructions",
        "recipeName",
        "recipeList",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        recipe_list = RecipeIndex.objects.get(id=self.kwargs["recipe_id"])
        initial_data["recipe_list"] = recipe_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        recipe_list = RecipeIndex.objects.get(id=self.kwargs["recipe_id"])
        context["recipe_list"] = recipe_list
        context["recipeName"] = "Add a new recipe"
        context["recipe_instructions"] = "Add instructions"
        return context

    def get_success_url(self):
        return reverse("recipe-index", args=[self.object.recipeList_id])
    