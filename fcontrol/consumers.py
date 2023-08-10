# chat/consumers.py
import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer

class SensorDataConsumer(AsyncJsonWebsocketConsumer):
    # процедура подключения к веб-сокету
    async def  connect(self):
        user = self.scope['user']
        print(user) #перемення включающая информацию от пользователя
        await self.accept()
        await self.channel_layer.group_add('sensor_data',self.channel_name) # если группы нет то она создатстся либо подключимся к ней если она уже есть

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, content : dict, **kwargs):
        print(content)
    async def sensor_data_handler(self, content:dict):
        print(content)

        await self.send_json(content=content)