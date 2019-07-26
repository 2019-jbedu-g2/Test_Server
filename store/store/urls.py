from django.conf.urls import url
from django.urls import path, include
from .views import StoreViewSet
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'', StoreViewSet, basename='store')
router.register('', StoreViewSet, basename='store')

urlpatterns = [
    # path('', include(router.urls))
    # path('<int:pk>/', views.index),

    # api_view url
    path('', views.store_list),             # 전체 가게 리스트
    path('<int:pk>/', views.store_detail),  # 가게 정보(대기열 포함)

    # APIView url
    # path('', views.StoreList.as_view()),
    # path('<int:pk>/', views.StoreDetail.as_view())
]
