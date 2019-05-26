from django.shortcuts import render
from django.views import generic
from .models import MainPost, Comment

def index(request):
    return render(
        request,
        'index.html',
    )

class MainPostView(generic.DetailView):
    model = MainPost

class MainPostListView(generic.ListView):
    model = MainPost
    paginate_by=10