from .models import Storedb, Accountdb
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storedb
        fields = '__all__'


class StoreManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountdb
        fields = '__all__'



