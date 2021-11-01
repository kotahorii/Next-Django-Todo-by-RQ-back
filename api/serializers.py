from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User, Tag, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True,
                                     'required': True, 'min_length': 5}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        models = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(
        source='user.username', read_only=True
    )
    tag_name = serializers.ReadOnlyField(
        source='tag.name', read_only=True
    )

    class Meta:
        model = Task
        fields = ('id', 'title', 'content', 'user',
                  'username', 'tag', 'tag_name')
