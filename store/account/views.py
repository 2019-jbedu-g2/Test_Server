from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Storedb, Queuedb, Accountdb
from .serializers import QueueSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
import time as t
# Create your views here.


# id 체크
def checkid(request, id, pwd):
    # id 인자와 일치하는 레코드를 검색하여 레코드에서 storenum, storepwd 값을 가져옴.
    store = Accountdb.objects.filter(storeid=id).values('storenum', 'storepwd')
    # 리스트형태로 넘어오지만 단일 객체이므로 0인덱스 값과 리스트 안에 딕셔너리의 키값으로 value를 가져옴.
    storenum = store[0]['storenum']
    storepwd = store[0]['storepwd']
    storename = Storedb.objects.get(storenum=storenum)

    if storepwd != pwd:
        return HttpResponse('아이디랑 비밀번호가 다릅니다.')
    else:
        return HttpResponse("%s, %s" % (storenum, storename.storename))


# 오프라인 줄서기
def createoffline(request, pk, phonenum):
    store = Storedb.objects.get(storenum=pk)
    barcode = phonenum
    # barcode = int(t.time())
    status = '줄서는중'

    waitingoff = Queuedb(barcode=barcode, onoffline=1, storenum=store, status=status)
    waitingoff.save()

    q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중').values('createtime')
    q2 = Queuedb.objects.filter(storenum=pk, status='미루기').values('updatetime')
    q3 = q1.union(q2)
    return HttpResponse("%d, 현재 대기인원 수 : %d명" % (barcode, q3.count() - 1))


# 바코드 확인하기
def checkbarcode(request, barcode):
    try:
        # check = Queuedb.objects.get(barcode=barcode).update(status='완료', updatetime=datetime.datetime.now())
        barcode = Queuedb.objects.get(barcode=barcode)
        barcode.updatetime = datetime.datetime.now()
        barcode.status = '완료'
        barcode.save()
        return HttpResponse('완료되었습니다.')
    except:
        return HttpResponse('바코드가 일치하지 않습니다.')


# 바코드 취소하기
def cancelbarcode(request, barcode):
    try:
        # cancel = Queuedb.objects.get(barcode=barcode).update(status='취소', updatetime=datetime.datetime.now())
        barcode = Queuedb.objects.get(barcode=barcode)
        barcode.updatetime = datetime.datetime.now()
        barcode.status = '취소'
        barcode.save()
        return HttpResponse('취소되었습니다.')
    except:
        return HttpResponse('바코드가 일치하지 않습니다.')

# 해당 가게의 대기열 리스트
@api_view(['GET'])
def Queuelist(request, pk):

    if request.method == 'GET':
        queryset = Queuedb.objects.filter(storenum=pk).order_by('barcode')
        serializer = QueueSerializer(queryset, many=True)
        return Response(serializer.data)
