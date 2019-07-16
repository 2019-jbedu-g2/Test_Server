from .models import Storedb
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storedb
        fields = '__all__'

