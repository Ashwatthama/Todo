from django.http import HttpResponse  # pyright: ignore[reportMissingModuleSource]
from django.shortcuts import render  # pyright: ignore[reportMissingModuleSource]

def home(request):
    return render(request, 'home.html')
    #return HttpResponse("Hello, world. You're at the ToDo home page.")