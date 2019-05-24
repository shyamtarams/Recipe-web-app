from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.logout2.as_view(), name='logout2'),
]