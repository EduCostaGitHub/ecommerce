from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from product.models import Product, ProductType

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
        # get product variation id       
        p_id = self.request.GET.get('p_id')

        # if product variation not exist set error message and return to home
        if not p_id:
            messages.error(
                self.request,
                'Product not found!',
            )
            return redirect(reverse('product:list'))
        # get product ( product variation) to add to cart
        p_to_add = get_object_or_404(ProductType, id = p_id)

        #check if cart exist, if not save one
        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()
        #get cart, new or existing
        cart = self.request.session['cart']

        if p_id in cart:
            # TODO: product exist in cart
            pass
        else:
            # TODO: product does not exist in cart
            pass
        
        return HttpResponse(f'{p_to_add.product} {p_to_add.name}')

        # messages.error(
        #     self.request,
        #     'Testing error messages!'
        # )

        # return redirect(self.request.META['HTTP_REFERER'])

        

class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remove from Cart')

class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Cart ')
 
class Finalize(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalize')
 