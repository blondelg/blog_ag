"""blog_AG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>', views.lire, name='lire'),
    path('videos/', views.videos, name='videos'),
    path('images/', views.images, name='images_all'),
    path('images/<int:art_id>', views.images, name='images'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
