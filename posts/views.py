from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import PostForm
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


def CreateMoreView(request, id):
    post = Post.objects.get(id=id)

    context = {

        'post': post

    }

    return render(request, 'more.html', context)


'''
    model = Post
    form_class = PostForm
    template_name = 'more.html'
    success_url = reverse_lazy('more')
   
   '''