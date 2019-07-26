from .models import Queuedb
from rest_framework import serializers


# 모델에서 원하는 필드만 정하여 시리얼화 시킴.
class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queuedb
        fields = ('barcode', 'onoffline', 'status')
