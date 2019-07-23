from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse, Http404
from .models import Storedb, Queuedb
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import QueueSerializer
import time as t
import datetime

# Create your views here.


# class WaitingList(APIView):
#     def get(self, request, format=None):
#         queryset = Queuedb.objects.all()
#         serializer = QueueSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class WaitingDetail(APIView):
#     """ 바코드생성 """
#     def createbarcode(self, request, format=None):
#         barcode = int(t.time())
#
#         serializer = QueueSerializer(data=barcode)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def createbarcode(request, pk):
    store = Storedb.objects.get(storenum=pk)
    barcode = int(t.time())
    createtime = datetime.datetime.now()
    status = '줄서는중'

    waiting = Queuedb(barcode=barcode, onoffline=0, storenum=store, createtime=createtime, status=status)
    waiting.save()

    q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중').values('createtime')
    q2 = Queuedb.objects.filter(storenum=pk, status='미루기').values('updatetime')
    q3 = q1.union(q2)
    return HttpResponse("%d, 현재 대기인원 수 : %d명" % (barcode, q3.count() - 1))


def updatewaiting(request, pk, barcode):
    Cbarcode = Queuedb.objects.get(barcode=barcode)
    Cbarcode.updatetime = datetime.datetime.now()
    Cbarcode.status = '미루기'
    Cbarcode.save()

    q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중').values('createtime')
    q2 = Queuedb.objects.filter(storenum=pk, status='미루기').values('updatetime')
    q3 = q1.union(q2)
    return HttpResponse("%d, 현재 대기인원 수 : %d명" % (barcode, q3.count()-1))


def waitingconfirm(request, pk, barcode):
    try:
        Cbarcode = Queuedb.objects.get(barcode=barcode)
    except:
        return HttpResponse('해당 바코드는 없는 바코드입니다.')

    if Cbarcode.status == '완료' or Cbarcode.status == '취소':
        return HttpResponse('확인이 불가합니다.')
    else:
        q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중', createtime__lte=Cbarcode.updatetime).values('createtime')
        q2 = Queuedb.objects.filter(storenum=pk, status='미루기', updatetime__lte=Cbarcode.updatetime).values('updatetime')
        q3 = q1.union(q2)
        return HttpResponse("%d, 현재 대기인원 수 : %d명" % (barcode, q3.count()-1))


@api_view(['GET', 'POST'])
def waiting_list(request):
    # 전체 데이터 조회
    if request.method == 'GET':
        queryset = Queuedb.objects.all()
        # serializer = StoreSerializer(queryset, context={'request': request}, many=True)
        serializer = QueueSerializer(queryset, many=True)
        return Response(serializer.data)

    # 데이터 입력
    elif request.method == 'POST':
        serializer = QueueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse("잘못된 요청")


@api_view(['GET', 'PUT', 'DELETE'])
def waiting_detail(request, pk):
    try:
        waiting = Queuedb.objects.get(pk=pk)
    except:
        return HttpResponse("해당 데이터가 없")

    # 특정 데이터 조회
    if request.method == 'GET':
        serializer = QueueSerializer(waiting)
        return Response(serializer.data)

    # 특정 데이터 수정
    elif request.method == 'PUT':
        serializer = QueueSerializer(waiting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse("수정이 않")

    # 특정 데이터 삭제
    elif request.method == 'DELETE':
        waiting.delete()
        return HttpResponse('삭제 완')
