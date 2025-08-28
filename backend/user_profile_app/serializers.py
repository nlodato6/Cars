from rest_framework import serializers
from .models import UserProfile
from user_app.models import AppUser


class UserProfileSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(
        queryset=AppUser.objects.all())

    class Meta:
        model = UserProfile
        # You can use as many fields as you like from your model
        fields = ('account', 'street_name',
                  'street_number', 'zip_code', 'city')
