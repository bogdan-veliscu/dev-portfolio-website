from django.shortcuts import render
from .models import Project
# Create your views here.


def homepage(request):
    return render(request, 'projects/home.html')
