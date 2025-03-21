from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(help_text="Enter ingredients, separated by commas")
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    def __str__(self):
        return self.name



