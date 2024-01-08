# authentication/urls.py

from django.urls import path
from .views import user_login, user_logout , register

urlpatterns = [
    path('', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', register, name='register'),
    # Add other authentication-related URLs as needed
]
