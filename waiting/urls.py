from django.conf.urls import url
from django.urls import path, include
# from .views import StoreViewSet
from . import views
# from .views import fetch_store, CreateBarcode
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'', StoreViewSet, basename='store')
# router.register('', StoreViewSet, basename='store')

urlpatterns = [
    # path('', include(router.urls))
    # path('<int:pk>/', views.index),

    # api_view url
    path('', views.waiting_list),
    path('<int:pk>/', views.createbarcode),
    path('<int:pk>/<int:barcode>/', views.updatewaiting),
    path('confirm/<int:pk>/<int:barcode>/', views.waitingconfirm)

    # APIView url
    # path('', views.WaitingList.as_view()),
    # path('<int:pk>/', views.WaitingDetail.as_view())
]
