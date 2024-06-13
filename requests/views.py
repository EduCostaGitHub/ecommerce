from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.
class RequestPay(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')

class CloseRequest(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Close')
    

class RequestDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detail')

