from django.views.generic import ListView

from posts.models import Post

class GuestHomePageView(ListView):
    model = Post
    template_name = 'guest_home.html'
