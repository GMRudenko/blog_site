from django.shortcuts import render
from django.views import generic
from .models import MainPost, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateCommentForm, CreateMainPostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


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
                author = request.user
                Comment.objects.create_comment(
                    text=form.cleaned_data['text'],
                    author=author,
                    post=mainpost,
                    time=datetime.now()
                )
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

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url="/blog/"
    template_name="registration/register.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView,self).form_valid(form)

class MainPostListView(generic.ListView):
    model = MainPost
    paginate_by = 10


@login_required
def MainPostCreate(request):
    if request.method == 'POST':
        form = CreateMainPostForm(request.POST)
        if form.is_valid():
            author = request.user
            pk=MainPost.objects.create_mainpost(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                author=author,
                time=datetime.now(),
            ).id
            return HttpResponseRedirect(reverse('mainpost-detail',kwargs={'pk': pk}))
    else:
        form = CreateMainPostForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/mainpost_create.html', context)
