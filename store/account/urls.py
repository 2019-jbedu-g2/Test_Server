from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:pk>/', views.Queuelist),
    path('confirm/<int:barcode>/', views.checkbarcode),
    path('cancel/<int:barcode>/', views.cancelbarcode)
]