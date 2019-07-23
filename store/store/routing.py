from . import consumers
from django.urls import re_path


websocket_urlpatterns = [
 re_path(r'queue/(?P<storenum>.*)/(?P<username>.*)/')  ,
    consumers.UserTestConsumer
]
#https://github.com/stephenmcd/django-socketio