from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",)

def about(request):
    context={'f_name':"Taif",'l_name':"Hammad"}
    return render(request,"about.html",context)