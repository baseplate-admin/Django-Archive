import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
import jwt


# from django.core import serializers
async def validate(token):
    secret = settings.SECRET_KEY
    return_object = jwt.decode(str(token), secret, algorithms='HS256')
    return return_object


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
        # Convert this to dict
        data = json.loads(event["text"])
        # data['input'] <- Input data
        # data['jwt']['access'] <- JWT access key
        input_data = data['input']
        access_key = data['jwt']['access']
        x = (await validate(access_key))
        print(x)

    @database_sync_to_async
    def get_data(self):
        pass

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        await self.close()
