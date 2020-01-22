from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class MessageList(LoginRequiredMixin, APIView):
    def get(self, request):
        messages = Message.objects.all()[0:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MessageListDAH(LoginRequiredMixin, APIView):
    def get(self, request):
        messages = Message.objects.filter(tags__title='DAH')[:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MessageListUTG(LoginRequiredMixin, APIView):
    def get(self, request):
        messages = Message.objects.filter(tags__title='UTG')[:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MessageListS7(LoginRequiredMixin, APIView):
    def get(self, request):
        messages = Message.objects.filter(tags__title='S7')[:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MessageListBHG(LoginRequiredMixin, APIView):
    def get(self, request):
        messages = Message.objects.filter(tags__title='BHG')[:20]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self):
        pass
