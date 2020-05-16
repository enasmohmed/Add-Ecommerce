from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    url(r'^$', views.WishListView.as_view() , name='wishlist_detail'),
    url(r'^update/$', views.list_update , name='list_update'),
    url(r'^remove/$', views.list_remove , name='list_remove'),
]