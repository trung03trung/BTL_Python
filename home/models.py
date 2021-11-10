
from typing import cast
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime


# Create your models here.
statusChoice=((0,'Hết hàng'),(1,'Sale'),(2,'Mới'))
promotionChoice=((0,'Bình thường'),(1,'Nổi bật'))
class Category_parent(models.Model):
    catep_id=models.AutoField(primary_key='true')
    catep_name=models.CharField(max_length=100,null=False)
    date_create=models.DateField()
    class Meta:
        db_table='tb_CategoryParent'
    def __str__(self):
        return self.catep_name
class Category_chile(models.Model):
    listcatep=Category_parent.objects.all()
    result=[]
    for items in listcatep:
        result.append((items.catep_id,items.catep_name))
    catec_id=models.AutoField(primary_key='true')
    catec_name=models.CharField(max_length=100)
    catep_id=models.IntegerField(choices=result)
    date_create=models.DateField()
    class Meta:
        db_table='tb_CategoryChild'
    def __str__(self):
        return self.catec_name
class Product(models.Model):
    listcatep=Category_parent.objects.all()
    result=[]
    for items in listcatep:
        result.append((items.catep_id,items.catep_name))
    listcatec=Category_chile.objects.all()
    result1=[]
    for items in listcatec:
        result1.append((items.catec_id,items.catec_name))
    product_id=models.AutoField(primary_key='true')
    catep_id=models.IntegerField(choices=result)
    catec_id=models.IntegerField(choices=result1)
    product_name=models.CharField(max_length=300,null=False)
    product_image1=models.ImageField(null=False)
    product_image2=models.ImageField(null=True)
    product_image3=models.ImageField(null=True)                            
    status=models.SmallIntegerField(choices=statusChoice)
    promotion=models.SmallIntegerField(choices=promotionChoice,default=0)
    product_size=models.CharField(max_length=4,default="M")
    product_amount=models.IntegerField(default=0)
    date_create=models.DateField()
    description=models.TextField()
    product_price=models.FloatField(default=0)
    def __str__(self):
        return self.product_name
class UsercreateForm(UserCreationForm):
    email=forms.EmailField(required=True,label='Email',error_messages={'exist':'Email này đã tồn tại'})
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    def __init__(self, *args , **kwargs):
        super(UsercreateForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder']='Tên đăng nhập'
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['password1'].widget.attrs['placeholder']='Mật khẩu'
        self.fields['password2'].widget.attrs['placeholder']='Nhập lại mật khẩu'
    def save(self, commit=True):
       user=super(UsercreateForm,self).save(commit=False)
       user.email=self.cleaned_data['email']
       if commit:
           user.save()
       return user
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exist'])
        return self.cleaned_data['email']
class UserPassword(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    def __str__(self):
        return self.username
class Order(models.Model):
    Order_id=models.AutoField(primary_key='true')
    product=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField(default='')
    quantity=models.CharField(max_length=5)
    price=models.FloatField()
    size=models.CharField(max_length=4,default="M")
    total=models.FloatField(default=0)
    address=models.TextField()
    phone=models.CharField(max_length=12)
    date=models.DateField(default=datetime.datetime.today)
    def __str__(self):
        return self.name
