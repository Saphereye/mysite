from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog.html', {
        'name':'Herr Das',
    })

def easter_egg(request):
    return HttpResponse("Easter Egg 🥚")