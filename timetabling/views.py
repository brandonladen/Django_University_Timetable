from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'timetabling/index.html')

def signin(request):
    return render(request, 'timetabling/signin.html')

def signup(request):
    return render(request, 'timetabling/signup.html')