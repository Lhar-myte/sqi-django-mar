from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "bakery/homepage.html")

def about(request):
    return render(request, "bakery/about.html")

def contact_us(request):
    return render(request, "bakery/contact.html")

def menu(request):
    return render(request, "bakery/menu.html")

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # Handle email storage logic here
        print(f"New subscriber: {email}")  # Debugging (Remove in production)
        return HttpResponse("Subscription successful!")  # Temporary response

    return redirect('local_bakery:homepage')  # Redirect to homepage (or another page)
