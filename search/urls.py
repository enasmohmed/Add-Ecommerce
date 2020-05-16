from django.conf.urls import url

import Shop
from . import views
from .views import search

app_name = "search"

urlpatterns = [
    url(r'^$', search, name='search'),
]