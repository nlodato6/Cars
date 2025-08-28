from django.http import Http404, HttpResponseNotFound
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import AppUser
from .serializers import AppUserSerializer

# We will utilize serializer to turn our QuerySets into
# binary string
from django.core.serializers import serialize

# Json.loads will turn binary strings into JSON data
import json


class AllUsers(APIView):
    def get(self, request):
        users = AppUser.objects.order_by("last_name")
        serializer = AppUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelectedUser(APIView):
    def get_object(self, pk):
        try:
            return AppUser.objects.get(pk=pk)
        except AppUser.DoesNotExist:
            raise Http404

    #  Specify the method to trigger this behavior
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = AppUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # <-- ID is our url parameter
        try:
            user = self.get_object(pk)
        except AppUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
