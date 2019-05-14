from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "core/home.html")

def about(request):
     return render(request, "core/about.html")

def contact(request):
     return render(request, "core/contact.html")

def prueba(request):
     return render(request, "core/prueba.html")

def hello(request):
     return render(request, "core/hello.html")





