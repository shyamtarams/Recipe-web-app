from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from posts import views

urlpatterns = [
     path('admin/', admin.site.urls),


     path('accounts/', include('accounts.urls')),
     path('accounts/', include('django.contrib.auth.urls')),
     path('', include('posts.urls')),
     path('guest_home/', include('guest_home.urls')),
     path('user_profile/', include('user_profile.urls')),
     path('comments/', include('comments.urls')),
     path('social-auth/', include('social_django.urls', namespace="social")),
     # path('<int:recipe_id>/like/', views.like_post, name='like_post'),
     path('<int:id>', views.like_post, name="like_post"),
     #path('like/', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
