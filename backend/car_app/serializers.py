from rest_framework import serializers
from .models import Car, CarModel

class CarSerializer(serializers.ModelSerializer):
    car_model = serializers.PrimaryKeyRelatedField(
        queryset=CarModel.objects.all())

    class Meta:
        model = Car
        # You can use as many fields as you like from your model
        fields = ['number_of_owners', 'registration_number',
                  'manufacture_year', 'number_of_doors', 'car_model', 'mileage']
