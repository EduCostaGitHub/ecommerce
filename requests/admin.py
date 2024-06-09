from django.contrib import admin
from requests.models import Requests,ItemRequest

# Register your models here.

class RequestItemsInLine(admin.TabularInline):
    model = ItemRequest
    extra = 1

class RequestsAdmin(admin.ModelAdmin):
    inlines =[
        RequestItemsInLine,
    ]

admin.site.register(Requests, RequestsAdmin)
admin.site.register(ItemRequest)