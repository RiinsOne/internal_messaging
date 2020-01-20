from rest_framework import serializers
from .models import Message, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']


class MessageSerializer(serializers.ModelSerializer):
    date_pub = serializers.DateTimeField(format='%H:%M:%S %d.%m.%Y')
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ['title', 'tags', 'body', 'slug', 'date_pub']
