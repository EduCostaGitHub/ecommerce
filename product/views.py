from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from product.models import Product

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


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
 