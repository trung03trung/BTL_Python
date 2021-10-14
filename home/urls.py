from django import VERSION
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
urlpatterns = [
    path ('',views.index),
    path ('home',views.index,name='home'),
    path ('service',views.service),
    path('my-account',views.my_account),
    path('shop',views.shop),
    path('cart',views.cart),
    path('about',views.about),
    path('wishlist',views.wishlist),
    path('shop-detail.html',views.shop_detail),
    path('product<int:id>',views.product),
    path('shop-detail<int:id>',views.product_detail),
    path('checkout.html',views.checkout),
    path('signup',views.signup,name='signup'),
    path('account/',include('django.contrib.auth.urls'))
]