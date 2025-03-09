from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
  content = {
    'posts' : Post.objects.all()
  }
  return render(request,'blog_app/index.html',content)

def about(request):
  return render(request,'blog_app/about.html',{'title':'About'})

