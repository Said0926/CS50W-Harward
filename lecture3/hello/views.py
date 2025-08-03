from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(rewuest):
    # return HttpResponse('Hello, World!')
    return render(request, 'hello/index.html')

def brian(request):
    return HttpResponse('Hello, Brain!')

def david(request):
    return HttpResponse('Hello, David!')

def greet(request, name):
    return render(request, 'hello/greet.html', {
        'name': name.capitalize()
    })


