from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import store.routing
from django.conf.urls import url, include
application = ProtocolTypeRouter({
    #http->django views is added by default
    'websocket':URLRouter(
            store.routing.websocketpatterns
        )
})
urlpatterns = [
    url(r'^', include('store.urls'))
]