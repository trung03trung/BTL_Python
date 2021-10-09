from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index),
    path ('home',views.index),
    path ('service',views.service),
    path('my-account',views.my_account),
    path('shop',views.shop),
    path('cart',views.cart),
    path('about',views.about),
    path('wishlist',views.wishlist),
    path('shop-detail.html',views.shop_detail),
    path('product<int:id>',views.product),
    path('shop-detail<int:id>',views.product_detail)
]