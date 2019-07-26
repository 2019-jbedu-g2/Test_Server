from django.urls import path
from . import views

urlpatterns = [
    path('login/<str:id>/<str:pwd>/', views.checkid),
    path('<int:pk>/', views.Queuelist),
    path('off/<int:pk>/', views.createoffline),
    path('confirm/<int:barcode>/', views.checkbarcode),
    path('cancel/<int:barcode>/', views.cancelbarcode)
]
