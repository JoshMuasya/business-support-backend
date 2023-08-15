from rest_framework import serializers
from customer.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'