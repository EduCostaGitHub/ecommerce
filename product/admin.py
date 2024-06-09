from django.contrib import admin
from product.models import Product, ProductType


class ProductTypeInLine(admin.TabularInline):
    model = ProductType
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines =[
        ProductTypeInLine,
    ]

# Register your models here.

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductType)