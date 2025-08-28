from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound

# We will import the following to read and return JSON data more efficiently
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# We want to bring in our model
from .models import Car
from .serializers import CarSerializer

# We will utilize serializer to turn our QuerySets into
# binary string
from django.core.serializers import serialize

# Json.loads will turn binary strings into JSON data
import json

# Create your views here.


class AllCars(APIView):
    # Establish the method that will trigger this behavior
    def get(self, request):
        car = Car.objects.order_by("car_id")
        # we can't send back query sets as a valid JSON response
        # so we will utilize Django's built in serialize function
        # to turn our query set into a binary string
        serialized_car = serialize("json", car)
        # Now we can use the python json.loads function to turn
        # our binary string into a workable json format
        json_car = json.loads(serialized_car)
        return Response(json_car)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelectedCar(APIView):
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    #  Specify the method to trigger this behavior
    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # <-- ID is our url parameter
        try:
            car = self.get_object(pk)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
