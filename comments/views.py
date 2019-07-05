from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import auth




from .forms import PostComment
#from .models import Comment

class HomePageView(ListView):
    #model = Comment
    template_name = 'more_new.html'

class CreatePostView(CreateView):
    #model = Comment
    form_class = PostComment
    template_name = 'comment.html'
    success_url = reverse_lazy('more_new')

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/accounts/login")

'''
def CreateMoreView(request, id):
    post = Comment.objects.get(id=id)

    context = {

        'post': post

    }

    return render(request, 'more_new.html', context)

'''



