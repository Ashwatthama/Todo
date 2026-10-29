from django.shortcuts import render  # type: ignore[reportMissingModuleSource]
from django.http import HttpResponse  # type: ignore[reportMissingModuleSource]

# Create your views here.

def addTask(request):
    return HttpResponse("This is the add task page.")