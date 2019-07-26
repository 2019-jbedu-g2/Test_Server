from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import store.routing
from django.conf.urls import url, include
application = ProtocolTypeRouter({
    #http->django views is added by default
    #만약에 websocket protocol 이라면 authMiddlewareStack
    'websocket':URLRouter(
        #URLRouter로 연결, 소비자의 라우트 연결 HTTP path조사
            store.routing.websocket_urlpatterns
        )
})
urlpatterns = [
    url(r'^', include('store.urls'))
]