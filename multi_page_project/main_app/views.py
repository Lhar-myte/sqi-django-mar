from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "application/home.html")


def about_us(request):
    return render(request, "application/about.html")


def contact_us(request):
    return render(request, "application/contact.html")
