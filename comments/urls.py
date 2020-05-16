from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^$', views.CommentsView.as_view(), name='comment_list'),
    url(r'^create/$', views.CommentCreateView.as_view(), name='comment_create'),
]
