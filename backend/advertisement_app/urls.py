from django.urls import path, register_converter
# Explicit imports
from .views import AllAds, SelectedAd
# import our converter class to utilize as a parameter type
from .converters import IntOrStrConverter

# To use this custom converter in a URL pattern, you need to register it with Django using the register_converter function.
register_converter(IntOrStrConverter, 'int_or_str')

# Remember all urls are prefaced by http://localhost:8000/api/v1/advertisements/
urlpatterns = (
    # Currently only takes GET requests
    path('', AllAds.as_view(), name='all_ads'),
    path('<int:pk>/', SelectedAd.as_view(), name='an_ad')
)
