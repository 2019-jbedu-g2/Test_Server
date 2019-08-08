from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Queuedb
from .serializers import QueueSerializer

# send 등과 같은 동기적인 함수를 비동기적으로 사용하기 위해 async / await로 변경한다.


class Queuecheck(AsyncWebsocketConsumer):
    # 방 이름과 유저 바코드 번호 받는 변수 선언.
    room_name = ''
    user_name = ''
    # websocket이 연결 되었을때 행해질 메소드

    async def connect(self):
        # store/routing 에있는 url에서 가게 번호와 바코드 번호 가져오기.
        # room_name = 상점번호 , user_name = 발급된 바코드
        self.room_name = self.scope['url_route']['kwargs']['snum']
        self.room_group_name = 'chat_%s' % self.room_name
        # url로부터 접속한 인원이 누구인지 체크 함.
        self.user_name = self.scope['url_route']['kwargs']['unum']

        # 그룹에 join
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # 접속 수락
        await self.accept()

    # 연결이 끊길 경우.
    async def disconnect(self, a):
        # 그룹에서 떠나기.
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 클라이언트로부터 메세지를 받으면 행해질 메서드
    # 메세지를 받으면 다시 클라이언트로 메세지를 되돌려 줌.
    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': text_data
                }
            )

    async def chat_message(self, event):
        # 가게번호와 바코드번호를 각 클라이언트 별로 저장.
        pk = self.room_name
        barcode = self.user_name

        # 이벤트가 일어 날 때마다 연결된 모든 클라이언트들이 데이터를 다시 받아야 하나 서로 다른 값을 받아야 하므로
        # 가게인지 일반 클라이언트인지 구별하여 서로 필요한 값을 전송한다.
        if barcode == 'master':         # 가게일 경우엔 전체 대기열을 json으로 묶어 전송
            queryset = Queuedb.objects.filter(storenum=pk).order_by('barcode')
            serializer = QueueSerializer(queryset, many=True)
            message = serializer.data
        else:
            try:
                Cbarcode = Queuedb.objects.get(barcode=barcode)
                if Cbarcode.status == '완료' or Cbarcode.status == '취소':  # 완료 처리 되거나 취소 처리된 바코드의 경우.
                    message = '확인이 불가합니다.'
                elif Cbarcode.status == '줄서는중':                         # 줄서는 중 일경우 (온라인/오프라인 모두)
                    q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중', createtime__lte=Cbarcode.createtime).values('createtime')
                    q2 = Queuedb.objects.filter(storenum=pk, status='미루기', updatetime__lte=Cbarcode.createtime).values('updatetime')
                    q3 = q1.union(q2)
                    message = q3.count() - 1
                else:                                                       # 미루기 상태 일경우.
                    q1 = Queuedb.objects.filter(storenum=pk, status='줄서는중', createtime__lte=Cbarcode.updatetime).values('createtime')
                    q2 = Queuedb.objects.filter(storenum=pk, status='미루기', updatetime__lte=Cbarcode.updatetime).values('updatetime')
                    q3 = q1.union(q2)
                    message = q3.count() - 1
            except:                                                         # 바코드 번호가 검색되지 않는 경우
                message = '해당 바코드는 없는 바코드입니다.'

        # 해당 검색 결과들을 그룹 내 모든 사람들에게 JSON형식으로 전송한다.
        await self.send(text_data=json.dumps({
            'message': message
        }, ensure_ascii=False))
