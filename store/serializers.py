from .models import Storedb, Accountdb, Storeview
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storedb
        fields = '__all__'


class StoreManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountdb
        fields = '__all__'


class StoreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storeview
        fields = '__all__'
