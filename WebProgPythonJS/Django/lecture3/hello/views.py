from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!") 

def iago(request):
    return HttpResponse("Hello, Iago!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
