from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse

# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return HttpResponse(blog)
