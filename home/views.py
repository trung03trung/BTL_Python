from django.shortcuts import render
from django.http import HttpResponse
from .models import Category_parent,Category_chile,Product
# Create your views here.


def index(request):
    return render(request,'pages/index.html')
def service(request):
    return render(request,'pages/service.html')
def my_account(request):
    return render(request,'pages/my-account.html')
def shop(request):
    listcp=Category_parent.objects.all()
    listcc=Category_chile.objects.all()
    listproducts=Product.objects.all()
    return render(request,'pages/shop.html',{'categoriesP':listcp,'categoriesC':listcc,'products':listproducts})
def cart(request):
    return render(request,'pages/cart.html')
def about(request):
    return render(request,'pages/about.html')
def wishlist(request):
    return render(request,'pages/wishlist.html')
def shop_detail(request):
    return render(request,'pages/shop-detail.html')
def product(request,id):
    listcp=Category_parent.objects.all()
    listcc=Category_chile.objects.all()
    productcat=Product.objects.filter(catec_id=id)
    return render(request,'widgets/product.html',{'categoriesP':listcp,'categoriesC':listcc,'products':productcat})
def product_detail(request,id):
    detail=Product.objects.get(product_id=id)
    otherPro=Product.objects.filter(catec_id=detail.catec_id)
    return render(request,'pages/shop-detail.html',{'detail':detail,'otherpro':otherPro})