from django.shortcuts import render
from django.views import generic
from .models import MainPost, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateCommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(
        request,
        'index.html',
    )


def MainPostView(request, pk):
    mainpost = get_object_or_404(MainPost, pk=pk)
    if User.is_authenticated:
        if request.method == 'POST':
            form = CreateCommentForm(request.POST)
            if form.is_valid():
                author=request.user
                Comment.objects.create_comment(
                    form.cleaned_data['text'], author=author, post=mainpost)
                return HttpResponseRedirect(reverse('mainpost-detail', kwargs={'pk': pk}))
        else:
            form = CreateCommentForm()
        context = {
            'form': form,
            'mainpost': mainpost
        }
    else:
        context = {
            'mainpost': mainpost
        }

    return render(request, 'blog/mainpost_detail.html', context)


class MainPostListView(generic.ListView):
    model = MainPost
    paginate_by = 10


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
