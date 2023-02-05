from django.shortcuts import render
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from .models import *
# #############################################
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products
    }
    return render(request,'home.html',context=context)
def product_detail(request,id):
    product = Product.objects.get(id =id)
    albums = Album.objects.filter(product=product)
    print(albums)
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'product':product,
        'albums':albums
    }
    return render(request,'products.html',context=context)
def category_detail(request,id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    products = category.products.all()
    context = {
        'category':category,
        'products':products,
        'categories':categories,
       
    }
    return render(request,'category.html',context=context)
    
# Create your views here.
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response