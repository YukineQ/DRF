from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.url', 'blog'), namespace='blog')),
    path('', include(('blog_api.url', 'blog_api'), namespace='blog_api')),
]
