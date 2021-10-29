from django.contrib.auth.forms import UsernameField
from django.db.models import query
from django.shortcuts import  redirect, render
from django.http import HttpResponseRedirect
from .models import Category_parent,Category_chile, Order,Product,UsercreateForm,UserPassword
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User
# from .forms import

# Create your views here.


def index(request):
    product_new=Product.objects.filter(status=2)
    product_f=Product.objects.filter(promotion=1)
    return render(request,'pages/index.html',{'product_new':product_new,'product_featured':product_f})
def service(request):
    return render(request,'pages/service.html')
def shop(request):
    listcp=Category_parent.objects.all()
    listcc=Category_chile.objects.all()
    listproducts=Product.objects.all()
    return render(request,'pages/shop.html',{'categoriesP':listcp,'categoriesC':listcc,'products':listproducts})
def about(request):
    return render(request,'pages/about.html')
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
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        for i in cart:
            a=float(cart[i]['price'])
            b=cart[i]['quantity']
            total=a*b
            order=Order(
                user=user,
                name=name,
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                total=total,
                address=address,
                phone=phone,

            )
            order.save()
        request.session['cart']={}
        return redirect('home')

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
@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(product_id=id)
    cate_id=product.catec_id
    cart.add(product=product)
    return redirect("product",id=cate_id)


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(product_id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(product_id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(product_id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
def your_order(request):
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(pk=uid)
    order=Order.objects.filter(user=user)
    
    return render(request,'pages/order.html',{'yourOder':order})
def search(request):
    query=request.GET['query']
    product=Product.objects.filter(product_name__icontains=query)
    context={
      'products':product,
    }
    return render(request,'pages/search.html',context)
def buy_new(request,id): 
    product=Product.objects.get(product_id=id)
    total=product.product_price+30000
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        uid=request.session.get('_auth_user_id')        
        user=User.objects.get(pk=uid)
      
        order=Order(
                user=user,
                name=name,
                product=product.product_name,
                price=product.product_price,
                quantity=1,
                image=product.product_image1,
                total=product.product_price,
                address=address,
                phone=phone,

            )
        order.save()
        return redirect('home')

    return render(request,'cart/buynew.html',{'product':product,'total':total})
