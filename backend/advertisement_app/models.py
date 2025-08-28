from django.db import models

class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    advertisement_date = models.DateTimeField(auto_now_add=True)
    seller_account = models.ForeignKey(
        'user_app.AppUser', on_delete=models.CASCADE)
    car = models.ForeignKey('car_app.Car', on_delete=models.CASCADE)

    class Meta:
        ordering = ('advertisement_id',)

    def __str__(self):
        return f''' advertisement_date: {self.advertisement_date} | seller_account_id: {self.seller_account} | car_id: {self.car} '''
