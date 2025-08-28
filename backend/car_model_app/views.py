from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from rest_framework.views import APIView, Response
from rest_framework import status

# We want to bring in our model
from .models import CarModel
from .serializers import CarModelSerializer

# We will utilize serializer to turn our QuerySets into binary string
from django.core.serializers import serialize

# Json.loads will turn binary strings into JSON data
import json

# Create your views here.


class AllCarModels(APIView):
    # Establish the method that will trigger this behavior
    def get(self, request):
        model = CarModel.objects.order_by("make")
        serialized_model = serialize("json", model)
        json_model = json.loads(serialized_model)
        return Response(json_model)

    def post(self, request, format=None):
        serializer = CarModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelectedModel(APIView):
    def get_object(self, pk):
        try:
            return CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404

    #  Specify the method to trigger this behavior
    def get(self, request, pk, format=None):
        model = self.get_object(pk)
        serializer = CarModelSerializer(model)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # <-- ID is our url parameter
        try:
            model = self.get_object(pk)
        except CarModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CarModelSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
