from django.urls import path

from .views import HomePageView, CreatePostView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('<int:id>/', views.CreateMoreView, name='more'),

]
