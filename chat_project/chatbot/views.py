from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
from .serializers import ConversationSerializer
from .models import Conversation
import openai
import os
import jwt
from chat_project.settings import SECRET_KEY
from django.shortcuts import get_object_or_404

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


class ChatView(APIView):
    def get(self, request):
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        user = payload.get('user_id')

        conversations = Conversation.objects.filter(user=user)
        serialized_conversations = ConversationSerializer(conversations, many=True)
        return Response(serialized_conversations.data)

    
    def post(self, request):
        prompt = request.POST.get('prompt')
        access = request.COOKIES['access']
        
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        user = payload.get('user_id')

        model_engine = "text-davinci-003"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=5,
            stop=None,
            temperature=0.5
        )
        response = completions.choices[0].text.strip()
        data = {'prompt': prompt, 'response': response}

        serializer = ConversationSerializer(data=data)
        if serializer.is_valid():
            conversation = serializer.save(user=user)
            conversation.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)