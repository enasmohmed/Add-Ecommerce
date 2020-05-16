from django.conf.urls import url

# from Shop.views import MainCategory

from.import views

app_name ='Shop'

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^list/$', views.product_list, name='product_list'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^contact/$', views.AboutUs, name='about'),
    url(r'^change-language/$', views.change_language, name='change-language'),
]

