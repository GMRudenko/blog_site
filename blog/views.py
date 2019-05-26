from django.shortcuts import render
from django.views import generic
from .models import BlogPost

class BlogListView(generic.ListView):
    model = 
    context_object_name = 'blog_list'
    paginate_by = 10