from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import serializers
from .models import Tag, Task


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)


class LoginUserView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (AllowAny,)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (AllowAny,)


class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (AllowAny,)


class TaskCreateView(generics.CreateAPIView):
    serializer_class = serializers.TagSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'GET method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
