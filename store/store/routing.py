from django.conf.urls import url
from channels.routing import route_pattern_match
from . import queue
#from channels import include, route
from .queue import Queuecheck

urlpatterns = [
    url('^',queue.Queuecheck)
]
'''
websocket_routing =[
    route_pattern_match("websocket.connect",Queuecheck.connect),
    route_pattern_match("websocket.receive",Queuecheck.receive),
    route_pattern_match("websocket.disconnect",Queuecheck.disconnect),
]
'''
#https://github.com/stephenmcd/django-socketio