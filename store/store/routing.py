from . import queue
from django.urls import re_path

# 웹소켓 urlpatterns.
websocket_urlpatterns = [
    re_path(r'queue/(?P<snum>[^/]+)/(?P<unum>[^/]+)', queue.Queuecheck),    # queue/가게번호/바코드번호로 접속
    re_path(r'queue/', queue.Queuecheck)                                    # 웹소켓 접속 여부 확인용 URL
]