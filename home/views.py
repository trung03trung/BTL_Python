from django.shortcuts import  redirect, render
from django.http import HttpResponseRedirect
from .models import Category_parent,Category_chile,Product,UsercreateForm,UserPassword
from django.contrib.auth import authenticate,login
# from .forms import

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
def checkout(request):
    return render(request,'pages/checkout.html')
def signup(request):
    if request.method=='POST':
        form=UsercreateForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            new_user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request,new_user)
            UserPassword(username=form.cleaned_data['username'],password=form.cleaned_data['password1']).save()
            return redirect('home')
    
    else:
        form=UsercreateForm()
    return render(request,'widgets/signup.html',{'form':form})