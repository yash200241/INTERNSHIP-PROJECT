# submission/urls.py
# urls.py in your app
from django.urls import path
from .views import submit_paper,home
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('submit-paper/', submit_paper, name='submit-paper'),
    path('home/', home, name='home'),
    path('submit_paper', views.submit_paper, name="submit_paper"),
]

