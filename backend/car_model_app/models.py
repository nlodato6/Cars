from django.db import models

class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    make = models.CharField(blank=False, max_length=50,
                            unique=False, default=None)
    model = models.CharField(blank=False, max_length=50,
                             unique=True, default=None)

    class Meta:
        ordering = ('car_model_id',)

    def __str__(self):
        return f''' make: {self.make} | model: {self.model} '''
