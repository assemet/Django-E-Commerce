from django.contrib import admin
from .models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','parent','status']
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','category','status']
    list_filter = ['category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
