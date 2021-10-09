from typing import cast
from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
statusChoice=((1,'Con hang'),(0,'Het hang'))
class Category_parent(models.Model):
    catep_id=models.AutoField(primary_key='true')
    catep_name=models.CharField(max_length=100,null=False)
    status=models.SmallIntegerField(choices=statusChoice)
    date_create=models.DateField()
    class Meta:
        db_table='tb_CategoryParent'
class Category_chile(models.Model):
    listcatep=Category_parent.objects.all()
    result=[]
    for items in listcatep:
        result.append((items.catep_id,items.catep_name))
    catec_id=models.AutoField(primary_key='true')
    catec_name=models.CharField(max_length=100)
    catec_image=models.ImageField()
    catep_id=models.IntegerField(choices=result)
    status=models.SmallIntegerField(choices=statusChoice)
    date_create=models.DateField()
    class Meta:
        db_table='tb_CategoryChild'
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
    pro_price=models.CharField(max_length=10)                            
    status=models.SmallIntegerField(choices=statusChoice)
    date_create=models.DateField()
    description=models.TextField()