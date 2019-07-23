from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer

def announce_likes(sender, instance, created, **kwargs):
    if created:
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "shares", {
                "type": "share_message",
                "message": instance.message,
            }
        )

class Queuecheck(WebsocketConsumer):
    #websocket이 연결 되었을때 행해질 메소드
    def connect(self):
        self.groupname = "shares"
        self.accept()
        self.send(text_data=json.dumps({
            'test': '테스트',
        }))
        #self.receive("test")
    #연결이 끊길 경우.
    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.groupname,
            self.channel_name
        )
    #클라이언트로부터 메세지를 받으면 행해질 메서드
    #아래에서는 메세지를 받으면 다시 클라이언트로 보내는 코드를 작성한 예시이다.
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['clientMessage']
        print(message)
        Num = 5
        while(Num >0):
            # 이 부분이 클라이언트로 다시 메세지를 보내는 부분이다.
           self.send(text_data=json.dumps({
              'Storename' : '테스트상점',
               'Barcode' : '12345678',
               'Number' :  Num
           }))
           Num-=1
           time.sleep(5)
