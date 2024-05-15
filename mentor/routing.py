from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/blogreviewcreation/<int:blog_id>/', consumers.BlogReviewConsumer.as_asgi()),
    path('ws/blogreviewreplycreation/<int:blog_review_id>/', consumers.BlogReviewReplyConsumer.as_asgi()),
]