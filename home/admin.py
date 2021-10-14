from django.contrib import admin
from . models import Category_parent,Category_chile,Product, UserPassword
# Register your models here.
class cpAdmin(admin.ModelAdmin):
    list_display=['catep_name']
    search_fields=['catep_name']
class ccAdmin(admin.ModelAdmin):
    list_display=['catec_name']
    search_fields=['catec_name']
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name']
    search_fields=['product_name']
admin.site.register(Category_parent,cpAdmin)
admin.site.register(Category_chile,ccAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(UserPassword)