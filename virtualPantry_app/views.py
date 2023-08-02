from django.views.generic import ListView
from .models import FoodList

class ListListView(ListView):
    model = FoodList
    template_name = "virtualPantry_app/index.html"