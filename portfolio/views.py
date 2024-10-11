from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects':projects})

def aboutme(request):
    return render(request, 'aboutme.html')

def home_view(request):
    return render(request, 'home.html')