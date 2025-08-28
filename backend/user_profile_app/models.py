from django.db import models

class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    street_name = models.CharField(
        blank=False, max_length=255, unique=False, default=None)
    street_number = models.CharField(
        blank=False, max_length=255, unique=False, default=None)
    zip_code = models.CharField(
        blank=False, max_length=5, unique=False, default=None)
    city = models.CharField(blank=False, max_length=50,
                            unique=False, default=None)
    account = models.ForeignKey('user_app.AppUser', on_delete=models.CASCADE)

    class Meta:
        ordering = ('profile_id',)

    def __str__(self):
        return f'''| profile_id: {self.profile_id} | {self.account} | street_name: {self.street_name} | street_number: {self.street_number} | zip_code: {self.zip_code} | city: {self.city} |'''
