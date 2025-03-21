from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe

def recipe_details(request, recipe_id):
    recipe_dt = get_object_or_404(Recipe, id = recipe_id)
    return render(request, "recipe_apps/recipe_details.html", {"recipe_dt": recipe_dt})

def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_app:list_of_recipes') 
    else:
        form = RecipeForm()

    return render(request, 'recipe_apps/add_recipe.html', {'form': form})

def list_of_recipe(request):
    list_of_recipes = Recipe.objects.all()
    return render(request, "recipe_apps/list_of_recipe.html", {"list_of_recipes": list_of_recipes})


# def manual_form_plus_django_form(request):
#     context = {
#         "form": form
#     }    

    # return render(request,"recipe_app/manual-form-plus-django-form.html", context)

def manual_form_plus_django_form(request):
    form = RecipeForm()
    all_recipe = Recipe.objects.all()


    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_app:list_of_recipes')

    context = {
        "form": form,
        "recipe": all_recipe,
    }
    return render(request, "recipe_apps/manual-form-plus-django-form.html", context)
   