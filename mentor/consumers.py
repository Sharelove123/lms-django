import json

from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

#rom .models import Room, Message
from .models import Blog, BlogReview,Student

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = self.scope['url_route']['kwargs']['blog_id']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        print('connected')
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        userImg = data['userImg']
        studentId = data['studentId']
        blogId = data['blogId']

        await self.save_message(username, blogId, message,studentId)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'userImg':userImg,
                'studentId':studentId,
                
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        userImg = event['userImg']
        studentId = event['studentId']
        userImg = event['userImg']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'userImg':userImg,
            'studentId':studentId
        }))

    @sync_to_async
    def save_message(self, username, room, message,studentId):
        #user = User.objects.get(username=username)
        #room = Room.objects.get(slug=room)

        #Message.objects.create(user=user, room=room, content=message)
        student = Student.objects.get(id=studentId)
        blog = Blog.objects.get(id=room)
        BlogReview.objects.create(student=student, comment=message, blog=blog)