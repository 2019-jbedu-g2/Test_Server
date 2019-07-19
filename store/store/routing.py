from django.conf.urls import url
from . import queue
#from channels import include, route
#from .queue import connect, receive, disconnect

websocket_urlpatterns = [
    url(r'^/test/',queue.Queuecheck)
]
#websocket_routing =[
#    route("websocket.connect",connect),
#    route("websocket.receive",receive),
#    route("websocket.disconnect",disconnect),
#]