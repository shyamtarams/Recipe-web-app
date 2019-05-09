from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('',views.login,name="login")
    #path("<int:pk>/", views.details, name="details")
]