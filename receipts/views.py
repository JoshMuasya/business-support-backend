from rest_framework import generics
from receipts.models import Receipt
from receipts.serializers import ReceiptSerializer
import datetime
from rest_framework.response import Response

class ReceiptCreateView(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


class ReceiptRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer