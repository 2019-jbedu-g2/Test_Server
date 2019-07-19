from django.shortcuts import render
from django.http import HttpResponse
from .models import Storedb, Queuedb
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import StoreSerializer
# Create your views here.

def test(request):
    return render(request,'store/index.html',{})

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


def CreateBarcode(request, storenum):
    Queuedb.objects.create(barcode='001')

    wait_num = Queuedb.objects.filter(storenum=storenum)

    return HttpResponse("대기 인원 수: %d" % wait_num.count())


class StoreViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Storedb.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)