from django.urls import path
from .views import AllUsers, SelectedUser

# Remember all urls are prefaced by http://localhost:8000/api/v1/users/
urlpatterns = [
    path('', AllUsers.as_view(), name='all_users'),
    path('<int:pk>/', SelectedUser.as_view(), name='a_user'),
]
