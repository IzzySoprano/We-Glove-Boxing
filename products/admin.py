# Code adapted from the CI Boutique Ado mini project

from django.contrib import admin
from .models import (Product, Category, Gender, SubCategory
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'product_description',
        'price',
        'image',
    )
    ordering = ('sku', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Gender, GenderAdmin)