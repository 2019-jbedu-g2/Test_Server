from django.urls import path
# from .views import StoreViewSet
from . import views
from .views import fetch_store


urlpatterns = [
    # path('<storename>/', views.index),
    path('<storenum>/', fetch_store),
    path('', fetch_store)
]