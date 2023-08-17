from rest_framework import generics
from payments.models import Payments
from payments.serializers import PaymentSerializer
import datetime
from rest_framework.response import Response

class PaymentCreateView(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer