from django.conf.urls import url
from django.urls import path, include
from .views import StoreViewSet
from . import views
from .views import fetch_store, CreateBarcode
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', StoreViewSet, basename='store')


urlpatterns = [
    url(r'^', include(router.urls)),
    # path('<storename>/', views.index),
    path('<storenum>/', fetch_store),
    # path('<storenum>/', CreateBarcode),
    # path('', fetch_store)
    path('')
]