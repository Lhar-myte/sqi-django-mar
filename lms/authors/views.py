from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "author/home.html")
def book_list(request):
    return render(request, "author/book_list.html")