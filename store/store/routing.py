from . import queue
from django.urls import re_path


websocket_urlpatterns = [
# re_path(r'queue/(?P<storenum>.*)/(?P<username>.*)/',
    re_path(r'queue/',
    queue.Queuecheck),
]
#https://github.com/stephenmcd/django-socketio