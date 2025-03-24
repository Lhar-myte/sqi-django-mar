from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

class Book(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(5)])
    author = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    publication_date = models.DateField() 
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name = "reviews")
    reviewer_name =  models.CharField(max_length=255)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.reviewer_name} for {self.book.title}"

#    Fields: book (ForeignKey to Book), reviewer_name, rating (integer from 1 to 5), comment (Text), and created_at.
# For the created_at field, use models.DateTimeField(auto_now_add=True)
