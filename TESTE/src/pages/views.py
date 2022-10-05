from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_views(request,*arg,**kwarg):
    #return HttpResponse("<h1>Hello this is my site</h1>")
    return render(request,'home.html',{})