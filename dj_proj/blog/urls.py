from django.urls import path
from . import views

#from . represents the same directory

# good practice to leave the name as 'blog-home' since other apps can also have home pages
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
