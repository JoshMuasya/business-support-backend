"""
URL configuration for business project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path

from auth import views
from customer.views import CustomerCreateView, CustomerRetrieveUpdateDestroyView
from payments.views import PaymentCreateView, PaymentRetrieveUpdateDestroyView
from feenotes.views import FeenoteCreateView, FeenoteRetrieveUpdateDestroyView
from receipts.views import ReceiptCreateView, ReceiptRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    path('customer/', CustomerCreateView.as_view(), name = 'customer-create'),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name = 'customer-retrieve-update-destroy'),
    path('payment/', PaymentCreateView.as_view(), name = 'payment-create'),
    path('payment/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name = 'payment-retrieve-update-destroy'),
    re_path(r'^feenote/$', FeenoteCreateView.as_view(), name='feenote-create'),
    re_path(r'^feenote/(?P<pk>\d+)/$', FeenoteRetrieveUpdateDestroyView.as_view(), name='feenote-retrieve-update-destroy'),
    path('receipt/', ReceiptCreateView.as_view(), name = 'receipt-create'),
    path('receipt/<int:pk>/', ReceiptRetrieveUpdateDestroyView.as_view(), name = 'receipt-retrieve-update-destroy'),
]
