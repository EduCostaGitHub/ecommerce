"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from requests.views import RequestPay,RequestSave,RequestDetail

app_name = 'request'

urlpatterns = [
        path('pay/', RequestPay.as_view() , name='pay'),
        path('close/', RequestSave.as_view() , name='close'),
        path('detail/<int:pk>', RequestDetail.as_view() , name='detail'),

] 