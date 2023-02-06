from django.shortcuts import render,redirect
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
# #############################################
def home(request):
    categories = Category.objects.all()
    try:
        products_list = Product.objects.all()
        paginated_products = Paginator(products_list, 1)
        page = request.GET.get('page', 1)
        products = paginated_products.page(page)
    except:
        return redirect('/')
    context = {
        'categories':categories,
        'products':products
    }
    return render(request,'home.html',context=context)
def product_detail(request,id):
    product = Product.objects.get(id =id)
    albums = Album.objects.filter(product=product)
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
    try:
        products_list = category.products.all()
        paginated_products = Paginator(products_list, 8)
        page = request.GET.get('page', 1)
        products = paginated_products.page(page)
    except:
        return redirect('/')
    context = {
        'category':category,
        'products':products,
        'categories':categories,
       
    }
    return render(request,'category.html',context=context)
def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        psw1=request.POST['psw1']
        user = authenticate(request,username=username,password=psw1)
        if user is not None:
           login(request,user) 
           return redirect('/')
        else:
            messages.error(request,"Username or Password incorrect!") 
            return redirect('/login') 
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect('/login')
def registerpage(request):
    if request.method=='POST':
        username=request.POST['username']
        psw1=request.POST['psw1']
        psw2=request.POST['psw2']
        if User.objects.filter(username=username).exists():
           messages.error(request,'This username already exists') 
           return redirect('/register') 
        if psw1!=psw2:
           messages.warning(request,"Password aren't match") 
           return redirect('/register')  
        else:
            User.objects.create_user(username=username,password=psw1)
            messages.success(request,"Profile created!")
            return redirect('/login') 
    return render(request,'register.html')    
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