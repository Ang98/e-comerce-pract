from django.contrib import admin

from products.models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','description','price','created','modified')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','created','modified')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display=('name','hex_code','created','modified')