from django.shortcuts import render
from django.shortcuts import render
from .models import Publisher


# Create your views here.

def index(request):
    return render(request, "base.html")


def home(request):
    return render(request, "home.html")


def about(request):
    name = {'fname': 'Ali', 'lname': 'Mushbari'}
    return render(request, "about.html", name)


def list_(request):
    list_ = Publisher.objects.all()
    context = {'list_': list_}
    return render(request, 'list_/about.html', context)
