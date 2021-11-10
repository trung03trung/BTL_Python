from django import VERSION
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path ('',views.index),
    path ('home',views.index,name='home'),
    path('shop',views.shop,name='shop'),
    path('about',views.about,name='about'),
    path('product<int:id>',views.product,name='product'),
    path('shop-detail<int:id>',views.product_detail,name='shop-detail'),
    path('checkout.html',views.checkout,name='checkout'),
    path('signup',views.signup,name='signup'),
    path('account/',include('django.contrib.auth.urls')),
     path('order/',views.your_order,name='order'),
     path('buy_new/<int:id>',views.buy_new,name='buy_new'),
     #add to cart
     path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
      path('cart/add_detail/<int:id>/', views.cart_add_detail, name='cart_add_detail'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('search/',views.search,name='search')
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)