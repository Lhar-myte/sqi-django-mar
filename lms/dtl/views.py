from django.shortcuts import render

# Create your views here.

def cart(request):
    context = {
        "user": "Olamide",
        "cart_items":["tomato", "strawberry", "vanoilla ice cream", "burger", "cake"],
        "is_favourite": True,
        "no_of_items_in_cart": 5,
    }
    return render(request, "dtl/cart.html", context)
