from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.http import Http404
from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer


class UsersList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = ReadOnlyUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WriteOnlyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(username=request.data['username'])
            serializer = ReadOnlyUserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetail(APIView):

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        serializer = ReadOnlyUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        print('put')
        user = self.get_object(id)
        serializer = WriteOnlyUserSerializer(user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(username=request.data['username'])
            serializer = ReadOnlyUserSerializer(user, many=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        print('patch')
        user = self.get_object(id)
        serializer = WriteOnlyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(username=request.data['username'])
            serializer = ReadOnlyUserSerializer(user, many=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
