from django.urls import path

from posts.views import GuestHomePageView


urlpatterns = [
    path('', GuestHomePageView.as_view(), name='guest_home'),
    #path('', GuestHomePageView.as_view, name='guest_home')
]
