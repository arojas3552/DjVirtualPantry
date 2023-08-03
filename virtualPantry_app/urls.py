# djvirutalpantry/virtualPantry_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("food/<int:food_id>/",
        views.ItemListView.as_view(), name="food_list"),
]