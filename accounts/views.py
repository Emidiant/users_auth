from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer


@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def users_list(request):
    if request.GET:
        if request.method == 'GET':
            user = User.objects.filter(id=request.GET['id'])
            serializer = ReadOnlyUserSerializer(user, many=True)
            return Response(serializer.data)
        elif request.method == 'PUT':
            user = User.objects.filter(id=request.GET['id'])
            serializer = ReadOnlyUserSerializer(user, many=True)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            user = User.objects.filter(id=request.GET['id'])
            serializer = ReadOnlyUserSerializer(user, many=True)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            user = User.objects.filter(id=request.GET['id'])
            serializer = ReadOnlyUserSerializer(user, many=True)
            return Response(serializer.data)
    else:
        if request.method == 'GET':
            users = User.objects.all()
            serializer = ReadOnlyUserSerializer(users, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = WriteOnlyUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




