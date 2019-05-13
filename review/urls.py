
from django.urls import path
from django.contrib import admin

from review import views as responseapp_views

urlpatterns = [
 path('response/', responseapp_views.responseform),
 path('response/', responseapp_views.responseform),
 #path('', admin.site.urls),
]