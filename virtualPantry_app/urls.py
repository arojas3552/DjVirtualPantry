# djvirutalpantry/virtualPantry_app/urls.py
from django.urls import path
from virtualPantry_app import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    
    path("list/<int:list_id>/",
        views.ItemListView.as_view(), name="list"),

    # CRUD patterns for FoodLists
    path("list/add/", views.ListCreate.as_view(), name="list-add"),

    path(
        "list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"
    ),

    # CRUD patterns for Products
    path(
        "list/<int:list_id>/item/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),

    path(
        "list/<int:list_id>/item/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),

    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="item-delete",
    ),

    #RECIPE feature
    
    
    path(
        "recipe/<int:index_id>/",
        views.RecipeIndexView.as_view(),
        name="recipe-index",
    ),

    path(
        "recipe/<int:index_id>/recipeid/<int:recipe_id>/",
        views.RecipeIngredientView.as_view(),
        name="recipe-view",
    ),

    #ADD 
    path(
        "recipe/add/",
        views.RecipeIndexCreate.as_view(),
        name="recipeIndex-add",
    ),
    path(
        "recipe/<int:index_id>/recipeid/add",
        views.RecipeCreate.as_view(),
        name="recipe-add",
    ),
    path(
        "recipe/<int:index_id>/recipeid/<int:recipe_id>/ingredient/add/",
        views.IngredientCreate.as_view(),
        name="ingredient-add",
    ),
    

]