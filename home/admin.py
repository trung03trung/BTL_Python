from django.contrib import admin
from . models import Category_parent,Category_chile,Product
# Register your models here.
admin.site.register(Category_parent)
admin.site.register(Category_chile)
admin.site.register(Product)