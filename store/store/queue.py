from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
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

class Queuecheck(AsyncWebsocketConsumer):
    #websocket이 연결 되었을때 행해질 메소드
    async def connect(self):
        # store/routing 에있는 url에서 roomname 가져오기.
        self.room_name = self.scope['url_route']['kwargs']['snum']
        self.room_group_name= 'chat_%s' %self.room_name
        #그룹에 join
        # send 등과 같은 동기적인 함수를 비동기적으로 사용하기 위해 async to sync로 합친다.
        self.accept()
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        self.send(text_data=json.dumps([{
            'storename': '2104030245',
        }]))
        #self.receive("test")
    #연결이 끊길 경우.
    async def disconnect(self, a):
        #그룹에서 떠나기.
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        pass
    #클라이언트로부터 메세지를 받으면 행해질 메서드
    #아래에서는 메세지를 받으면 다시 클라이언트로 보내는 코드를 작성한 예시이다.
    async def receive(self, text_data):
        #text_data_json = json.loads(text_data)
        #message = text_data_json['clientMessage']
        #print(message)
        print(text_data)
        if (text_data == 'count'):
            await self.channel_layer.group_send(
                self.room_group_name,{
                    '당신의 순서는 5번째 입니다'
                }
            )
            # self.send(text_data=json.dumps(
            #     '당신의 순서는 5번째 입니다'
            # ))
        elif (text_data == 'handover'):
            await self.channel_layer.group_send(
                self.room_group_name,{
                    '미루어졌습니다.'
                }
            )
            # self.send(text_data=json.dumps(
            #     '미루어졌습니다.'
            # ))
        elif (text_data == 'list'):
            await self.channel_layer.group_send(
                self.room_group_name,{
                    '현재 리스트입니다..'
                }
            )
            # self.send(text_data=json.dumps(
            #     '현재 리스트입니다..'
            # ))
        elif (text_data == 'confirm'):
           await self.channel_layer.group_send(
                self.room_group_name,{
                    '승인 되었습니다.'
                }
            )
            # self.send(text_data=json.dumps(
            #      '승인 되었습니다.'
            # ))
        elif (text_data =='cancel'):
            await self.channel_layer.group_send(
                self.room_group_name,{
                     '삭제 되었습니다.'
                }
            )
            # self.send(text_data=json.dumps(
            #     '삭제 되었습니다.'
            # ))
        else:
            self.send(text_data=json.dumps(
                '에러 : 알 수 없는 명령어. 다시 확인하시기 바랍니다.'
            ))

    async def chat_message(self, event):
        message = event
        await self.send(text_data=json.dumps(
            message
        ))
        # Num = 5
        # while(Num >0):
        #     # 이 부분이 클라이언트로 다시 메세지를 보내는 부분이다.
        #    self.send(text_data=json.dumps([{
        #       'Storename' : '테스트상점',
        #        'Barcode' : '12345678',
        #        'Number' :  Num
        #    }]))
        #    Num-=1
        #    time.sleep(5)
