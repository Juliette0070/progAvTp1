from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(
        "<h1>Hello Django!</h1>"
        "<a href='/appTp1/contact'>Contact</a> - <a href='/appTp1/about'>About</a> - <a href='/appTp1/hello/you'>Hello</a>"
        )

def contact(request):
    return HttpResponse(
        "<h1>Contact us</h1>"
        "<a href='/appTp1/'>Home</a>"
        )

def about(request):
    return HttpResponse(
        "<h1>About us</h1>"
        "<a href='/appTp1/'>Home</a>"
        )

def hello(request, name):
    return HttpResponse(
        f"<h1>Hello {name}!</h1>"
        "<a href='/appTp1/'>Home</a>"
        )
