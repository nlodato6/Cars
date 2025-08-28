from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework.views import APIView, Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserProfileSerializer

# We will utilize serializer to turn our QuerySets into
# binary string
from django.core.serializers import serialize

# Json.loads will turn binary strings into JSON data
import json

class AllUserProfiles(APIView):
    def get(self, request):
        user_profile = UserProfile.objects.order_by("account_id")
        # we can't send back query sets as a valid JSON response
        # so we will utilize Django's built in serialize function
        # to turn our query set into a binary string
        serialized_user_profile = serialize("json", user_profile)
        # Now we can use the python json.loads function to turn
        # our binary string into a workable json format
        json_user_profile = json.loads(serialized_user_profile)
        return Response(json_user_profile)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelectedUserProfile(APIView):
    def get(
        self, request, pk
    ):  # <-- Notice pk is now a parameter and its value is being pulled straight from our URL
        # Lets initialize pokemon as None and give it a
        # corresponding query set depending on the pks type
        try:
            user_profile = None
            # pk is an int
            if type(pk) == int:
                user_profile = UserProfile.objects.get(pk=pk)
            # pk is a string
            else:
                user_profile = UserProfile.objects.get(name=pk.title())
            json_user_profile = serialize("json", [user_profile])
            serialized_user_profile = json.loads(json_user_profile)[0]
            return Response(serialized_user_profile)
        except UserProfile.DoesNotExist:
            return HttpResponseNotFound(f'User profile not found!')

    def put(self, request, id):  # <-- ID is our url parameter
        # we still want to grab a pokemon either by ID or by name
        profile = self.get(id)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
