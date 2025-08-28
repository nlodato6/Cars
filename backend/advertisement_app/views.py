from django.http import Http404

# pokemon_app/views.py
# We will import the following to read and return JSON data more efficiently
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# We want to bring in our model
from .models import Advertisement
from .serializers import AdvertisementSerializer

# Json.loads will turn binary strings into JSON data
import json

class AllAds(APIView):
    # Establish the method that will trigger this behavior
    def get(self, request):
        ads = Advertisement.objects.order_by("advertisement_id")
        serializer = AdvertisementSerializer(ads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelectedAd(APIView):
    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            raise Http404

    #  Specify the method to trigger this behavior
    def get(self, request, pk, format=None):
        ad = self.get_object(pk)
        serializer = AdvertisementSerializer(ad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # <-- ID is our url parameter
        try:
            ad = self.get_object(pk)
        except Advertisement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AdvertisementSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ad = self.get_object(pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
