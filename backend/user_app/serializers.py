from rest_framework import serializers
from .models import AppUser

class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        # You can use as many fields as you like from your model
        fields = ('first_name', 'last_name', 'email')
