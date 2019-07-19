from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import time

class Queuecheck(WebsocketConsumer):
    #websocket이 연결 되었을때 행해질 메소드
    def connect(self):
        self.accept()
        self.send(text_data=json.dums({
            'test': '테스트',
        }))
    #연결이 끊길 경우.
    def disconnect(self):
        pass
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
