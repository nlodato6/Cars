from django.urls import path
from .views import AllCarModels, SelectedModel

# Remember all urls are prefaced by http://localhost:8000/api/v1/car_models/
urlpatterns = [
    # Currently only takes GET requests
    path('', AllCarModels.as_view(), name='all_car_models'),
    path('<int:pk>/', SelectedModel.as_view(), name='a_car_model'),
]
