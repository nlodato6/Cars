from django.urls import path
from .views import AllCars, SelectedCar

# Remember all urls are prefaced by http://localhost:8000/api/v1/cars/
urlpatterns = [
    path('', AllCars.as_view(), name='all_cars'),
    path('<int:pk>/', SelectedCar.as_view(), name='a_car'),
]
