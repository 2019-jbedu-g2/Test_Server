from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse, Http404
from .models import Storedb, Queuedb
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import QueueSerializer

# Create your views here.


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
    except Queuedb.DoesNotExit:
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
