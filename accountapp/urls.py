from django.urls import path
from accountapp.views import hello_world, hello_world_drf

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('hello_world_drf/', hello_world_drf, name='hello_world_drf'),
]