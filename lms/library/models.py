from django.db import models

# Create your models here.
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = "books")
    number_of_pages = models.PositiveBigIntegerField()
    published_on = models.DateField()



    def __str__(self):
        return f"{self.title} by {self.author}"
    
