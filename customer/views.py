from rest_framework import generics
from customer.models import Customers
from customer.serializers import CustomerSerializer
import datetime
from rest_framework.response import Response


class CustomerCreateView(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer