from django.shortcuts import render, HttpResponse

# Create your views here.
def menu(request):
    return HttpResponse("chek all menu")

def contact(request):
    return HttpResponse("contact us on: 0905656565")