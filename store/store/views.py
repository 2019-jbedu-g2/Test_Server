from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse, Http404
from .models import Storedb, Queuedb
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import StoreSerializer

# Create your views here.


def index(request, storename):
    return HttpResponse("Hello, world. You're at the {} index".format(storename))

def queuecheck(request, pk):
    q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중')
    q2 = Queuedb.objects.filter(storenum=pk, status='미루기')
    q3 = q1.union(q2)
    return HttpResponse("현재 대기인원 수 : %d명" % (q3.count()))

def waitingcnt(request, pk):
    q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중')
    q2 = Queuedb.objects.filter(storenum=pk, status='미루기')
    q3 = q1.union(q2)
    return HttpResponse("현재 대기인원 수 : %d명" % (q3.count()))

""" api_view Ex. (FBV기반) """
@api_view(['GET', 'POST'])
def store_list(request):
    # 전체 데이터 조회
    if request.method == 'GET':
        queryset = Storedb.objects.all()
        # serializer = StoreSerializer(queryset, context={'request': request}, many=True)
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)

    # 데이터 입력
    elif request.method == 'POST':
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse("잘못된 요청")


@api_view(['GET', 'PUT', 'DELETE'])
def store_detail(request, pk):
    try:
        store = Storedb.objects.get(pk=pk)
    except:
        return HttpResponse("해당 데이터가 없")

    # 특정 데이터 조회
    if request.method == 'GET':
        serializer = StoreSerializer(store)

        return Response(serializer.data)

    # 특정 데이터 수정
    elif request.method == 'PUT':
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return HttpResponse("수정이 않")

    # 특정 데이터 삭제
    elif request.method == 'DELETE':
        store.delete()
        return HttpResponse('삭제 완')


# """ APIView Ex. """
# class StoreList(APIView):
#     """ 전제 데이터 조회 """
#     def post(self, request, format=None):
#         serializer = StoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request, format=None):
#         queryset = Storedb.objects.all()
#         serializer = StoreSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class StoreDetail(APIView):
#     """ 특정 데이터 """
#     def get_object(self, pk):
#         try:
#             return Storedb.objects.get(pk=pk)
#         except:
#             return HttpResponse("해당 가게는 없습니다.")
#
#     """ 특정 데이터 조회 """
#     def get(self, request, pk):
#         store = self.get_object(pk)
#         serializer = StoreSerializer(store)
#         return Response(serializer.data)
#
#     """ 특정 데이터 수정 """
#     def put(self, request, pk, format=None):
#         store = self.get_object(pk)
#         serializer = StoreSerializer(store, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error_messages)
#
#     """ 특정 데이터 삭제 """
#     def delete(self, request, pk, format=None):
#         store = self.get_object(pk)
#         store.delete()
#         return HttpResponse("%s가 삭제되었습니다." % pk)


""" ViewSet Ex. """
# class StoreViewSet(viewsets.ModelViewSet):
#     queryset = Storedb.objects.all().order_by('-storenum')
#     serializer_class = StoreSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#
#         search = self.request.query_params.get('storenum', '')
#         if search:
#             qs = qs.filter(storenum=search)
#
#         return qs


class StoreViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Storedb.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)