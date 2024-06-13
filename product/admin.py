from django.contrib import admin
from product.models import Product, ProductType


class ProductTypeInLine(admin.TabularInline):
    model = ProductType
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = 'name', 'short_description','get_price_formated','get_promo_price_formated',   
    inlines =[
        ProductTypeInLine,
    ]
    prepopulated_fields={
        'slug':('name',),
    }

# Register your models here.

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductType)