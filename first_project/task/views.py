from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome to my homepage")

def all_task(request):
    return HttpResponse("do all task")
