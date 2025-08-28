from django.urls import path
from .views import AllUserProfiles, SelectedUserProfile

# Remember all urls are prefaced by http://localhost:8000/api/v1/user_profiles/
urlpatterns = [
    path('', AllUserProfiles.as_view(), name='all_user_profiles'),
    path('<int:pk>/', SelectedUserProfile.as_view(), name='a_user_profile'),
]
