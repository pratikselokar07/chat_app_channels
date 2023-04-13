from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Chat_app_consumer(AsyncWebsocketConsumer):
    # async def connect(self):
    #     print('Websocket Connected...')
    #     print("channel Layer..",self.channel_layer)
    #     self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        
    #     await self.channel_layer.group_add(
    #         self.group_name,
    #         self.channel_name
    #     )
    #     await self.accept()

    # async def receive(self, text_data):
    #     print('Message received from Client...',text_data)
    #     data=json.loads(text_data)
    #     message = data['message']
    #     await self.channel_layer.group_send(
    #         self.group_name,
    #         {
    #             'type':'chat_message',
    #             'message': message
    #         }
    #     ) 
    
    # async def chat_message(self,event):
    #     print("Event...", event)
    #     await self.send(text_data=json.dumps({
    #         'message':event['message']
    #     }))
    # async def disconnect(self, close_code):
    #     print('Websocket Disconnected...',close_code)
    #     print("Channel Layer", self.channel_layer)
    #     print("Channel Name", self.channel_name)
    #     await self.channel_layer.group_discard(
    #         self.group_name,
    #         self.channel_name
    #     )
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print(self.scope)
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))


# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
# import json

# class Testconsumer(WebsocketConsumer):

#     def connect(self):
#         self.room_name="test_consumer"
#         self.room_group_name="test_consumer_group"
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#         self.accept()
#         self.send(text_data=json.dumps({'status':'connected from django'}))

#     def receive(self, text_data):
#         print(text_data)
#         self.send(text_data=json.dumps({'status': 'We got you'}))

#     def disconnect(self, *args, **kwargs):
#         print('disconnected')
    
#     def send_notification(self, event):
#         print("send_notification")
#         data=json.loads(event.get('value'))
#         self.send(text_data=json.dumps({'payload':data}))
#         print("send_notification")

        # async def connect(self):
        # print('Websocket Connected...')
        # print("channel Layer..",self.channel_layer)
        # print("Channel Name..",self.scope['url_route']['kwargs']
        #       ['groupkaname'])
        # print("Group Name...",self.group_name)
        # async_to_sync(self.channel_layer.group_add)(
        #     self.group_name,
        #     self.channel_name
        # )
        # await self.accept()