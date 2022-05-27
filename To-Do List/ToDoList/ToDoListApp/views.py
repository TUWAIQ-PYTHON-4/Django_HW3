from django.shortcuts import render

# Create your views here.

def base (request):
    return render(request,"base.html")

def home (request):
    return render(request,"home.html")

def about (request):
    f_n = "Abdullah"
    l_n = "aqeel"
    return render(request,"about.html",{"f_n":f_n, "l_n":l_n})
