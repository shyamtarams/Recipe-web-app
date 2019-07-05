

from django.urls import path

from .views import HomePageView, CreatePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='user_profile'),
    path('upload/', CreatePostView.as_view(), name='add_post')
]
