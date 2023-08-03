from django.views.generic import ListView
from .models import FoodList, Product

class ListListView(ListView):
    model = FoodList
    template_name = "virtualPantry_app/index.html"


class ItemListView(ListView):
    model = Product
    template_name = "virtualPantry_app/virtualPantry_list.html"

    def get_queryset(self):
        return Product.objects.filter(food_list_id=self.kwargs["food_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["food_list"] = FoodList.objects.get(id=self.kwargs["food_id"])
        return context