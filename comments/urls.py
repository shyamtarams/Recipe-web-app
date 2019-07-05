from django.urls import path

#from posts.views import HomePageView, CreatePostView
from . import views
from .views import HomePageView, CreatePostView
from . import views

urlpatterns = [
    #path('', HomePageView.as_view(), name='more_new'),
    #path('post/', CreatePostView.as_view(), name='add_post'),
    #path('<int:id>/', views.CreateMoreView, name='more_new'),
   # path('<int:id>/', views.CreateMoreView, name='more_new'),
    path('comments/', CreatePostView.as_view(), name='add_post'),
    path('', HomePageView.as_view(), name='more_new'),
    path('logout/', views.logout, name='logout'),

    #path('post/', CCreatePostView.as_view(), name='add_post'),
    #path('<int:id>/', views.CCreateMoreView, name='more_new'),

]
