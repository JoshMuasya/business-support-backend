from rest_framework import generics, filters
from feenotes.models import Feenotes
from feenotes.serializers import FeenoteSerializer
import datetime
from rest_framework.response import Response

class FeenoteCreateView(generics.ListCreateAPIView):
    serializer_class = FeenoteSerializer
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = Feenotes.objects.all()
        customer = self.request.query_params.get('customer')
        if customer is not None:
            queryset = queryset.filter(customer=customer)
        return queryset


class FeenoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feenotes.objects.all()
    serializer_class = FeenoteSerializer