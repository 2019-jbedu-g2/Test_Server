from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Queuedb
from .serializers import QueueSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def Queuelist(request, pk):
    queue = Queuedb.objects.filter(storenum=pk)
    serializer = QueueSerializer(queue, many=True)
    return Response(serializer.data)
