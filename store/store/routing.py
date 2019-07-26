from . import queue
from django.urls import re_path


websocket_urlpatterns = [
    re_path(r'queue/(?P<snum>[^/]+)/(?P<unum>[^/]+)', queue.Queuecheck),
    re_path(r'queue/', queue.Queuecheck)
]
#https://github.com/stephenmcd/django-socketio