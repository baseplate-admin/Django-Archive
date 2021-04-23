import json


from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

# from django.core import serializers


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = "socket"

        await self.channel_layer.group_add(self.room_name, self.channel_name)

        await self.accept()

    async def receive(self, text_data):

        await self.channel_layer.group_send(
            self.room_name, {"type": "chat_message", "text": text_data}
        )

    async def chat_message(self, event):
        print(event)

    @database_sync_to_async
    def get_data(self):
        pass

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        await self.close()
