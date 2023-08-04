from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView,CreateView,UpdateView,DeleteView)

from .models import FoodList, Product

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