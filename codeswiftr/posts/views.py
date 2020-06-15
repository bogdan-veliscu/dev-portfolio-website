from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here


def latest_posts(request):
    return render(request, 'posts/latest_posts.html')
