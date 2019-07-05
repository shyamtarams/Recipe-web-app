from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import Post

from django.core.mail import send_mail




class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        f = form.save(commit=True)
        f.author = self.request.user
        f.save()
        return super(CreatePostView, self).form_valid(form)

    '''def like_post(request):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        post.likes.add(request.user)
        return HttpResponse(Post.get_absolute_url())'''


def CreateMoreView(request, id):
    post = Post.objects.get(id=id)
    #comments = Comment.objects.filter(post=post).order_by('-id')
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {

        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
        #'liked_names' : post.likes_name(),
        #'comment': comments,


    }
    #post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #post.likes.add(request.user)
    return render(request, 'more_new.html', context)


def like_post(request, id):

    post = Post.objects.get(id=id)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
                'post': post,
                'is_liked': is_liked,

                }
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        is_liked = True
    post.likes.add(request.user)
    return render(request, 'more_new.html', context)


class GuestHomePageView(ListView):
    model = Post
    template_name = 'guest_home.html'

class PromiseCreateView(CreateView):
    model = Post
    form_class = 'PostForm'






