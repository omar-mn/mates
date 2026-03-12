from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.response import Response


class MessageConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        user = self.scope['user']

        if user.is_authenticated :
            await self.accept()
        else:
            await self.close()
    
    async def disconnect(self, code):
        pass

    async def receive(self, text_data = None, bytes_data = None):
        print("data recived")