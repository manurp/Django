from django.shortcuts import render
from .models import Post
# Some dummy posts --> not required now
# posts = [
#     {'author': 'Manoj',
#      'title': 'First Post',
#      'content': 'Something..',
#      'date_posted': 'September 05,2018'},

#     {'author': 'Manoj',
#      'title': 'Second Post',
#      'content': 'Some Content',
#      'date_posted': 'September 05,2018'}
# ]

# Create your views here.

# request should be there as a parameter


def home(request):
    # render inturn returns HttpResponse
    # in views.py the function should return a HttpResponse or error
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
