from django.shortcuts import render

# Some dummy posts
posts = [
    {'author': 'Manoj',
     'title': 'First Post',
     'content': 'Something..',
     'date_posted': 'September 05,2018'},

    {'author': 'Manoj',
     'title': 'Second Post',
     'content': 'Some Content',
     'date_posted': 'September 05,2018'}
]

# Create your views here.

# request should be there as a parameter


def home(request):
    # render inturn returns HttpResponse
    # in views.py the function should return a HttpResponse or error
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
