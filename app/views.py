from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    return render(request,"home.html")

def dash1(request):
    return render(request,"dashboard1.html")

def dash2(request):
    return render(request,"dashboard2.html")

def dash3(request):
    return render(request,"dashboard3.html")

def dash4(request):
    return render(request,"dashboard4.html")

def vis1(request):
    return render(request,"visualize1.html")

def vis2(request):
    return render(request,"visualize2.html")

def vis3(request):
    return render(request,"visualize3.html")

def vis4(request):
    return render(request,"visualize4.html")

def story1(request):
    return render(request,"story1.html")

def story2(request):
    return render(request,"story2.html")

def report1(request):
    return render(request,"report1.html")

def report2(request):
    return render(request,"report2.html")