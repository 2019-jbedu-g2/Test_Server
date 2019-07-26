from .models import Queuedb
from rest_framework import serializers


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queuedb
        fields = '__all__'
