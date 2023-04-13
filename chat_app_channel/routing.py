from django.urls import path
from myapp.consumers import Chat_app_consumer

websocket_urlpatterns = [
    path('ws/awsc/<str:groupkaname>/', Chat_app_consumer.as_asgi()),
    path('ws/awsc/', Chat_app_consumer.as_asgi()),
]
