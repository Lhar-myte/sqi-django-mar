from django.shortcuts import render, HttpResponse

# Create your views here.
def my_app(request):
    return HttpResponse("welcome")