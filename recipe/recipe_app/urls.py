from django.urls import path
from . import views

app_name = 'recipe_app'


urlpatterns = [
    path('add/', views.add_recipe, name='add_recipe'),  # Make sure this is correctly set
    path('recipe-details/<int:recipe_id>',views.recipe_details, name='recipe_details'),  # Make sure this is correctly set
    path('list_of_recipes/',views.list_of_recipe, name='list_of_recipes'), 
    path('manual_form_plus_django_form/', views.manual_form_plus_django_form, name="manual_form_plus_django_form"),
] 