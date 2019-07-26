from .models import Storedb, Accountdb, Storeview, Queuedb
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


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queuedb
        fields = ('barcode', 'onoffline', 'status')

