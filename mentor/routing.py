from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/blogreviewcreation/<int:blog_id>/', consumers.BlogReviewConsumer.as_asgi()),
]