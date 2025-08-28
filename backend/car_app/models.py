from django.db import models
from car_model_app.models import CarModel

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    number_of_owners = models.IntegerField(blank=False, unique=False, default=None)
    registration_number = models.CharField(blank=False, max_length=8, unique=True, default=None)
    manufacture_year = models.IntegerField(blank=False, unique=False, default=None)
    number_of_doors = models.IntegerField(blank=False, unique=False, default=5)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    mileage = models.IntegerField(blank=False, default=None)

    class Meta:
        ordering = ('car_model', 'car_id')

    def __str__(self):
        return f''' number_of_owners: {self.number_of_owners} | registration_number: {self.registration_number} 
    | manufacture_year: {self.manufacture_year} | number_of_doors: {self.number_of_doors} | car_model: {self.car_model} 
    | mileage: {self.mileage} '''
