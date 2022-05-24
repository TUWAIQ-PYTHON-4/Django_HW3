from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    x = {'f_name':'Rahaf','l_name':'Adel'}
    return render(request, 'about.html',x)
