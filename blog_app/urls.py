"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import (LoginView,PasswordResetView)
from django.views.generic.base import RedirectView

from django.conf import settings
from blog_app.views import (
    # LoginView,
	PostList,
	post_detail,
    PostCreateView,
    PostViewSet,
    contact,)

from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'inputpost',PostViewSet)
urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    # path('', RedirectView.as_view(pattern_name='Home', permanent=False)),
    path('forgot-password/',PasswordResetView.as_view(),name="password_reset"),
    path('admin/', admin.site.urls),
    path('',PostList.as_view(),name='Home'),
    path('contact/',contact,name='Contact'),
    path('<slug>/',post_detail,name='PostDetail'),
    path('blog/create/',PostCreateView.as_view(),name='CreateBlog'),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
