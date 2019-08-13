from django.urls import path
from . import views


# conf 에서 넘어온 urls/에서 다시 분기시켜줌.
urlpatterns = [
    path('login/<str:id>/<str:pwd>/', views.checkid),    # 로그인
    path('<int:pk>/', views.Queuelist),                  # 가게 대기열 리스트
    path('off/<int:pk>/<int:phonenum>/', views.createoffline),          # 오프라인 줄서기
    path('confirm/<int:barcode>/', views.checkbarcode),  # 바코드 확인하기
    path('cancel/<int:barcode>/', views.cancelbarcode)   # 바코드 취소하기
]
