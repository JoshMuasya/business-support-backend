from rest_framework import serializers
from feenotes.models import Feenotes

class FeenoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feenotes
        fields = '__all__'