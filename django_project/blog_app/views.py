from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

contents = [
  {
    'author' : 'Sushant',
    'title' : 'Python Programming',
    'body' : 'This a blog about python',
    'date' : '24 jan'
  },
  {
    'author' : 'Bisakha',
    'title' : 'Java Programming',
    'body' : 'This a blog about java',
    'date' : '24 feb'
  }
]
def home(request):
  content = {
    'posts' : contents
  }
  return render(request,'blog_app/index.html',content)

def about(request):
  return render(request,'blog_app/about.html',{'title':'About'})

