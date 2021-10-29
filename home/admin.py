from django.contrib import admin
from . models import Category_parent,Category_chile, Order,Product, UserPassword
# Register your models here.
class cpAdmin(admin.ModelAdmin):
    search_fields=['catep_name']
class ccAdmin(admin.ModelAdmin):
    search_fields=['catec_name']
class ProductAdmin(admin.ModelAdmin):
    search_fields=['product_name']
admin.site.register(Category_parent,cpAdmin)
admin.site.register(Category_chile,ccAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(UserPassword)
admin.site.register(Order)