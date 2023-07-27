from django.urls import path
from .views import *

app_name = 'chatbot'

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat')
]