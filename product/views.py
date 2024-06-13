from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.

class ProductList(View):
    def get(self, *args, **kwargs):
        return HttpResponse('List Products')

class ProductDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Product Detail')

class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Add To Cart')

class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remove from Cart')

class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Cart ')
 
class Finalize(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalize')
 