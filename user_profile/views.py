

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Upload

class HomePageView(ListView):
    model = Upload
    template_name = 'user_profile.html'

class CreatePostView(CreateView):
    model = Upload
    form_class = PostForm
    template_name = 'post1.html'
    success_url = reverse_lazy('user_profile')
