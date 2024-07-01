from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from product.models import ProductType

import pprint

# Create your views here.
class RequestPay(View):
    template_name = 'request/pay.html'

    def get(self, *args, **kwargs):
        #get cart
        cart = self.request.session.get('cart')  
        #messages
        msg_error_no_stock=''
        
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'You need to login',
            )
            return redirect('profile:create')        

        if not cart:
            messages.error(
                self.request,
                'Cart is empty!',
            )
            return redirect('product:list')        
              
        cart_ProductTypes_ids = [v for v in cart]            

        bd_ProductTypes = list(
            ProductType.objects.select_related('product')
            .filter(id__in=cart_ProductTypes_ids)
        )

        for pT in bd_ProductTypes:
            _id = str(pT.pk)
            stock = pT.stock

            cart_qty = cart[_id]['qty']
            unit_price = cart[_id]['unit_price']
            promo_price = cart[_id]['promo_price']

           

            if stock < cart_qty:
                cart[_id]['qty'] = stock
                cart[_id]['qty_price'] = stock * unit_price
                cart[_id]['qty_promo_price'] = stock * promo_price

                msg_error_no_stock = ('Not enougth stock for some products, '
                    'quantity adjusted to stock available, '
                    'please check your cart'
                )

            if msg_error_no_stock:
                messages.error(
                    self.request,
                    msg_error_no_stock,                    
                )
                self.request.session.save()

                return redirect('product:cart')
                    
               

        context = {}

        return render(
            self.request,
            self.template_name,
            context,
        )

class RequestSave(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Close')
    

class RequestDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detail')

