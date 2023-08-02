from django.urls import path
from .views import *

app_name = 'chatbot'

urlpatterns = [
    path('chat/', Chat.as_view(), name='chat'),
    path('chatview/', ChatView.as_view(), name='chatview')
]