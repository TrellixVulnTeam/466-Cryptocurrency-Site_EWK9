from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def register(request):
    return render(reuqest, "register.html",{})

def login(request):
    return render(request, "login.html", {})

def about(request):
    return render(request, "about.html",{})
