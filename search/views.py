from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from Shop.models import Product
# Create your views here.

from django.shortcuts import render
from django.db.models import Q

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(name__icontains=q)
        context = {'query': q,
                   'products': products}
        template = 'temp/search.html'
    else:
        template = 'temp/search.html'
        context = {}
    return render(request, template, context)