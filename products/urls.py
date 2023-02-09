from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('product/<int:id>/',product_detail),
    path('category/<int:id>/',category_detail),
    path('register',registerpage,name='register'),
    path('login',loginpage,name='login'),
    path('logout',logoutUser),
    path('update_item/',update),
    path('cart',mycart)
]
