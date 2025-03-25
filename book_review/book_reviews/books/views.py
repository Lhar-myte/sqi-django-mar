from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ReviewForm, ReviewManualForm, UpdateReviewForm
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




def update_review_with_model_form(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    form = UpdateReviewForm(instance=review)

    if request.method == 'POST':
        form = UpdateReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()

            return redirect(reverse('books:book_details',kwargs={'book_id': review.book.id}))
           
    context = {
        "form": form,
        "review": review,
    }
    return render(request, "book_review/update_review_with_model_form.html", context)


def confirm_delete_review(request, review_id):

    review = get_object_or_404(Review, id=review_id)
    return render(request, "book_review/confirm-review-delete.html", {'review': review})



def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id )
    if request.method == 'POST':
        review.delete()
        return redirect("books:book_list")
    
    
    return redirect(reverse('books:book_details',kwargs={'book_id': review.book.id}))



