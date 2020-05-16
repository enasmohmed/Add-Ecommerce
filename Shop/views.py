from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import translation

import comments
from Shop.models import Category, Product, ProductImage
from cart.forms import CartAddProductForm
from django.utils.translation import ugettext as _
from django import http
from django.conf import settings
# Create your views here.
from comments.models import Comment


def Home(request):
    categories = Category.objects.filter(parent=None)
    featured_pro = Product.objects.filter(featured=True)
    popular_pro = Product.objects.filter(popular=True)
    comments = Comment.objects.filter(available=True)
    context = {
        'categories': categories,
        'featured_pro': featured_pro,
        'popular_pro': popular_pro,
        'comments': comments
    }
    return render(request, 'temp/index.html', context)

def product_list(request):
    categories = Category.objects.filter(parent=None)
    category = request.GET.get("category",None)
    if category:
        print(category)
        products = Product.objects.filter(available=True, category__full_name_string__icontains=category)
        fullname = category
        context = {
            'category': category,
            'categories': categories,
            'products': products,
            'fullname': fullname,
        }
    else:

        products = Product.objects.filter(available=True)

        page = request.GET.get('page', 1)

        paginator = Paginator(products, 10)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {
            'category': category,
            'categories': categories,
            'products': products,
        }

    return render(request, 'temp/shop-grid.html', context)



def product_detail(request,id,slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    related_pro = Product.objects.filter(related=True)
    upsell_pro = Product.objects.filter(upsell=True)
    cart_product_form = CartAddProductForm()
    context = {
		'product': product,
        'related_pro': related_pro,
        'upsell_pro':  upsell_pro,
		'cart_product_form': cart_product_form,
	}
    return render(request,'temp/product-detail.html',context)



def AboutUs(request):
    return render(request, 'temp/about-us.html')




def change_language(request):
    lang_code = request.GET.get('lang_code')

    response = http.HttpResponseRedirect(request.GET.get('return_url'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    translation.activate(lang_code)
    return response

