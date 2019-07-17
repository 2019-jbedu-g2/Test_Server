from django.shortcuts import render
from django.http import HttpResponse
from .models import Storedb
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import viewsets
from .serializers import StoreSerializer
# Create your views here.


def index(request, storename):
    return HttpResponse("Hello, world. You're at the {} index".format(storename))


# class StoreViewSet(viewsets.ModelViewSet):
#     queryset = Storedb.objects.all().order_by('storenum')
#     serializer_class = StoreSerializer

@api_view(['get'])
def fetch_store(request, storenum):
    stores = Storedb.objects.filter(storenum=storenum)
    serializer = StoreSerializer(stores, context={'request': request}, many=True)

    return Response(serializer.data)

