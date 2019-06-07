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

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        return super(CreatePostView, self).form_valid(form)

def CreateMoreView(request, id):
    post = Post.objects.get(id=id)

    context = {

        'post': post

    }

    return render(request, 'more_new.html', context)



class GuestHomePageView(ListView):
    model = Post
    template_name = 'guest_home.html'

class PromiseCreateView(CreateView):
    model = Post
    form_class = 'PostForm'

