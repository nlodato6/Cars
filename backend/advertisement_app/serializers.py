from rest_framework import serializers
from .models import Advertisement
from car_app.models import Car
from user_app.models import AppUser

class AdvertisementSerializer(serializers.ModelSerializer):
    seller_account = serializers.PrimaryKeyRelatedField(
        queryset=AppUser.objects.all())
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = Advertisement
        # You can use as many fields as you like from your model
        fields = ('advertisement_id', 'advertisement_date',
                  'seller_account', 'car')
