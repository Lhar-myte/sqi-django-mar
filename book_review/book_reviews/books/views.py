from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, ReviewManualForm
from .models import Book, Review

def book_list(request):
    book_list = Book.objects.all()
    return render(request, "book_review/book_list.html", {"book_list": book_list})


def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    form = ReviewForm()

    return render(request, 'book_review/book_details.html', {'book': book, 'reviews': reviews, 'form': form})



def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('books:book_details', book_id=book.id)
    else:
        form = ReviewForm()

    return render(request, 'book_review/book_details.html', {'book': book, 'form': form, 'reviews': book.reviews.all()})



def django_manual_form(request, book_id):
    form = ReviewManualForm()
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            reviewer_name = cleaned_data.get('reviewer_name')
            rating = cleaned_data.get('rating')
            comment = cleaned_data.get('comment')
            Review.objects.create(book=book, reviewer_name = reviewer_name, rating = rating, comment = comment)

            return redirect("books:book_details.html", id=book.id)
        
    context = {
        "book": book,
        'form': form, 
        'reviews': book.reviews.all()
    }
    return render(request,'book_review/django_manual_form.html', context)