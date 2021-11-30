from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from about.models import Data

def index(request):
    return render(request, "index.html")

def photo(request):
    data = Data.objects.all()
    context = {
        "datas": data
    }
    print(data)
    return render(request, "photo.html", context=context)

def about(request):
    with open('about/about.txt') as file:
        file2 = file.readlines()
        context = {
            "about": file2
        }
        return render(request, "about.html", context=context)

def contacts(request):
    with open('about/contacts.txt') as file:
        file2 = file.readlines()
        context = {
            "contacts": file2
        }
        return render(request, "contacts.html", context=context)