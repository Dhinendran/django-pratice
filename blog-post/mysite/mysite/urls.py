"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from .blog.views import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^post/$', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/(?P<pk>[0-9]+)/comment/$', views.post_comment, name='post_comment'),
    # url(r'^post/(?P<pk>[0-9]+)/comment/add_comment/$', views.add_comment, name='add_comment'),
    # url(r'^post/$', views.post_list, name='post_list'),
    url(r'',include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]
