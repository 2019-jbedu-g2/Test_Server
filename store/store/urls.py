from django.conf.urls import url
from django.urls import path, include
from .views import StoreViewSet
from . import views
from .views import fetch_store, CreateBarcode
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'', StoreViewSet, basename='store')
router.register('', StoreViewSet, basename='store')

urlpatterns = [
    # path('', include(router.urls))
    # path('<int:pk>/', views.index),

    # api_view url
    path('', views.store_list),
    path('<int:pk>/', views.store_detail),
    path('waitingcnt/<int:pk>/', views.waitingcnt)

    # APIView url
    # path('', views.StoreList.as_view()),
    # path('<int:pk>/', views.StoreDetail.as_view())
]