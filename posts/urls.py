from django.conf.urls import url, include
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^editor/', views.editor, name="editor"),
    url(r'^templates/', views.templates, name="templates"),
    #url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    #url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    #url(r'^user/(?P<fk>[0-9]+)', views.userposts, name='userposts'),
    #url(r'^$', views.home, name="home"),
]
