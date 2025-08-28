from rest_framework import serializers
from .models import CarModel
from car_app.serializers import CarSerializer


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # You can use as many fields as you like from your model
        fields = ('make', 'model')
