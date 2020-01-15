from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer


class MessageList(APIView):
    def get(self, request):
        messages = Message.objects.all()[0:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MessageListDAH(APIView):
    def get(self, request):
        messages = Message.objects.filter(tags__title='DAH')[:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MessageListUTG(APIView):
    def get(self, request):
        messages = Message.objects.filter(tags__title='UTG')[:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MessageListS7(APIView):
    def get(self, request):
        messages = Message.objects.filter(tags__title='S7')[:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass
