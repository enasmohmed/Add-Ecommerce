from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from Shop.models import Product
from wishlist.models import WishList


class WishListView(TemplateView):
    template_name = 'temp/wishlist-2.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WishListView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            wishlist, new_list = WishList.objects.new_or_get(self.request)
            list = wishlist.products.all()
            page = self.request.GET.get('page', 1)
            paginator = Paginator(list, 8)
            try:
                context['wishlist'] = paginator.page(page)
            except PageNotAnInteger:
                context['wishlist'] = paginator.page(1)
            except EmptyPage:
                context['wishlist'] = paginator.page(paginator.num_pages)
        else:
            context['wishlist'] = None
        return context

def list_update(request):
    if request.user.is_authenticated:
        wishlist, new_list = WishList.objects.new_or_get(request)
        product_id = request.POST.get('product_id')
        product_slug = request.POST.get('product_slug')
        product_name = request.POST.get('product_name')
        base_url = reverse('Shop:product_detail',args=[product_id,product_slug])
        url = '{}'.format(base_url)
        if product_id is not None:
            product = get_object_or_404(Product, id=product_id)
            if product in wishlist.products.all():
                wishlist.products.remove(product)
                msg = "{product} Removed From Wish List".format(product=product_name)
                messages.success(request, mark_safe(msg))
                return redirect(url)
            else:
                wishlist.products.add(product)
                msg = "{product} Added To Wish List".format(product=product_name)
                messages.success(request, mark_safe(msg))
                return redirect(url)
    else:
        return redirect("wishlist:wishlist_detail")



def list_remove(request):
    if request.user.is_authenticated:
        wishlist, new_list = WishList.objects.new_or_get(request)
        product_id = request.POST.get('product_id')
        if product_id is not None:
            product = get_object_or_404(Product, id=product_id)
            if product in wishlist.products.all():
                wishlist.products.remove(product)
                return redirect("wishlist:wishlist_detail")
    else:
        return redirect("wishlist:wishlist_detail")






