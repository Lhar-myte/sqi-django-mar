from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Author
from library.models import Book

# Create your views here.
def home(request):
    return render(request, "authors/home.html")

def book_list(request):
    return render(request, "authors/book-list.html")
    return render(request, "authors/book-list.html")


def authors_and_books(request):
    # all_authors = Author.objects.all()
    all_authors = Author.objects.order_by("first_name")
    by_birth_date = Author.objects.order_by("birth_date")
    all_books = Book.objects.all()
    try:
        author_with_id_1 = Author.objects.get(pk=1)
    except Author.DoesNotExist:
        author_with_id_1 = None
    agatha = Author.objects.get(pk=2)
    books_by_agatha = Book.objects.filter(author=agatha)
    authors_not_winnie = Author.objects.exclude(first_name="Winnie")
    books_not_by_agatha = Book.objects.exclude(author=agatha)
    authors_born_before_2000 = Author.objects.filter(birth_date__gt="2000-01-01")
    authors_born_in_2002 = Author.objects.filter(birth_date__year=2002)
    context = {
        "all_authors": all_authors,
        "books": all_books,
        "authors_by_birth_date": by_birth_date,
        "author_with_id_1": author_with_id_1,
        "books_by_agatha": books_by_agatha,
        "authors_not_winnie": authors_not_winnie,
        "books_not_by_agatha": books_not_by_agatha,
        "authors_born_before_2000": authors_born_before_2000,
        "authors_born_in_2002": authors_born_in_2002,
    }
    return render(request, "authors/authors-and-books.html", context)

# def author(request, author_id):
#     try:
#         author = Author.objects.get(id=author_id)
#     except Author.DoesNotExist:
#         return HttpResponse("Author not found")
#     return render(request, "authors/author-detail.html", {"author": author})


def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, "authors/author-detail.html", {"author": author})