from django.db import models
from user_profile_app.models import UserProfile
from django.core import validators as v

class AppUser(models.Model):
    account_id = models.AutoField(primary_key=True)
    first_name = models.CharField(
        blank=False, max_length=50, unique=False, default=None)
    last_name = models.CharField(
        blank=False, max_length=50, unique=False, default=None)
    email = models.EmailField(
        blank=False, max_length=155, unique=True, default=None)
    password = models.CharField(
        blank=False, max_length=255, unique=False, default=None)

    class Meta:
        ordering = ('account_id',)

    def __str__(self):
        return f''' account_id: {self.account_id} | first_name: {self.first_name} | last_name: {self.last_name} | email: {self.email} '''
