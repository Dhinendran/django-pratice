from django.conf.urls import url
# from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.post_comment, name='post_comment'),
    url(r'^post/(?P<pk>[0-9]+)/comment/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^post/$', views.post_list, name='post_list'),
    # url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
