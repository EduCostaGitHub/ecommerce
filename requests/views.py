from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from product.models import ProductType
from requests.models import Requests, ItemRequest
from utils import utils

class DispatchLoginRequired(DetailView):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('profile:create')

        return super().dispatch(*args, **kwargs)
    


# Create your views here.

class RequestPay(DetailView):
    template_name = 'request/pay.html'
    model= Requests
    pk_url_kwarg='pk'
    context_object_name = 'request'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('profile:create')
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs   
    

class RequestSave(View):
    
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
                        
            cart_total_qty = utils.cart_total_qtd(cart)       
            cart_total_value = utils.cart_total(cart)  

            request = Requests(
                user= self.request.user,
                total = cart_total_value,
                qtd_total=cart_total_qty,
                status='C',
            ) 

            request.save()

            ItemRequest.objects.bulk_create(
                [
                    ItemRequest(
                        request = request,
                        product = item['product_name'],
                        product_id = item['product_id'],
                        productType = item['pType_name'],
                        productType_id = item['pType_id'],
                        price = item['qty_price'],
                        promo_price = item['qty_promo_price'],
                        quantity = item['qty'],
                        image = item['image'],
                    )for item in cart.values()
                ]
            )   

            # context = {}

            # return render(
            #     self.request,
            #     self.template_name,
            #     context,
            # )

            del self.request.session['cart']
            return redirect(
                reverse(
                    'request:pay',
                    kwargs={
                        'pk': request.pk,
                    }
                )
            )

    
class RequestList(View):
    def get(self, *args, **kwargs):
        return HttpResponse('List')
    

class RequestDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detail')

