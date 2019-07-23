from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Queuedb, Storedb
from .serializers import QueueSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
import time as t
# Create your views here.


def createoffline(request, pk):
    store = Storedb.objects.get(storenum=pk)
    barcode = int(t.time())
    createtime = datetime.datetime.now()
    status = '줄서는중'

    waiting = Queuedb(barcode=barcode, onoffline=1, storenum=store, createtime=createtime, status=status)
    waiting.save()

    q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중').values('createtime')
    q2 = Queuedb.objects.filter(storenum=pk, status='미루기').values('updatetime')
    q3 = q1.union(q2)
    return HttpResponse("%d, 현재 대기인원 수 : %d명" % (barcode, q3.count() - 1))


def checkbarcode(request, barcode):
    try:
        barcode = Queuedb.objects.get(barcode=barcode)
        barcode.status = '완료'
        barcode.save()
        return HttpResponse('완료되었습니다.')
    except:
        return HttpResponse('바코드가 일치하지 않습니다.')


def cancelbarcode(request, barcode):
    try:
        barcode = Queuedb.objects.get(barcode=barcode)
        barcode.status = '취소'
        barcode.save()
        return HttpResponse('취소되었습니다.')
    except:
        return HttpResponse('바코드가 일치하지 않습니다.')


@api_view(['GET'])
def Queuelist(request, pk):
    queue = Queuedb.objects.filter(storenum=pk)
    serializer = QueueSerializer(queue, many=True)
    return Response(serializer.data)