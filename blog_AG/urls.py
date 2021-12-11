from django.contrib import admin
from django.urls import path, include
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('blog_app/', include('blog_app.urls')),
]
