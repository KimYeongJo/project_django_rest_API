from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat')
]