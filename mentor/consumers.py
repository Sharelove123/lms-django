import json

from django.contrib.auth.models import User
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

#rom .models import Room, Message
from .models import Blog, BlogReview,Student,Course,CourseReview,Product,ReviewProduct

class BlogReviewConsumer(AsyncWebsocketConsumer):
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
        print(f'{data} Recieved data')
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

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'userImg':userImg,
            'studentId':studentId,
        }))

    @sync_to_async
    def save_message(self, username, room, message,studentId):
        #user = User.objects.get(username=username)
        #room = Room.objects.get(slug=room)

        #Message.objects.create(user=user, room=room, content=message)
        student = Student.objects.get(id=studentId)
        blog = Blog.objects.get(id=room)
        BlogReview.objects.create(student=student, comment=message, blog=blog)
        
        
class CoursesReviewConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        print('connected courses comment')
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(f'{data} Recieved data')
        message = data['message']
        username = data['username']
        userImg = data['userImg']
        studentId = data['studentId']
        courseId = data['courseId']
        rating = data['rating']

        await self.save_message(username, courseId, message,studentId,rating)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'userImg':userImg,
                'studentId':studentId,
                'rating':rating,
                'created_at': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        userImg = event['userImg']
        studentId = event['studentId']
        rating = event['rating']
        created_at = event['created_at']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'userImg':userImg,
            'studentId':studentId,
            'rating':rating,
            'created_at':created_at
        }))

    @sync_to_async
    def save_message(self, username, courseId, message,studentId,rating):
        #user = User.objects.get(username=username)
        #room = Room.objects.get(slug=room)

        #Message.objects.create(user=user, room=room, content=message)
        student = Student.objects.get(id=studentId)
        course = Course.objects.get(id=courseId)
        CourseReview.objects.create(student=student, comment=message, course=course,rateing=rating)
 
        
  

class ProductReviewConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = self.scope['url_route']['kwargs']['product_id']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        print('connected product comment')
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(f'{data} Recieved data')
        message = data['message']
        username = data['username']
        userImg = data['userImg']
        userId = data['userId']
        productId = data['productId']
        rating = data['rating']

        await self.save_message(username, productId, message,userId,rating)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'userImg':userImg,
                'userId':userId,
                'rating':rating,
                'created_at': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        userImg = event['userImg']
        userId = event['userId']
        rating = event['rating']
        created_at = event['created_at']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'userImg':userImg,
            'userId':userId,
            'rating':rating,
            'created_at':created_at
        }))

    @sync_to_async
    def save_message(self, username, productId, message,userId,rating):
        #user = User.objects.get(username=username)
        #room = Room.objects.get(slug=room)

        #Message.objects.create(user=user, room=room, content=message)
        user = User.objects.get(id=userId)
        product = Product.objects.get(id=productId)
        ReviewProduct.objects.create(user=user, comment=message, product=product,rateing=rating)
 