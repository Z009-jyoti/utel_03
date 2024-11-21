from django.urls import path  # Only import path from django.urls
from . import views

app_name = 'rider'

urlpatterns = [
    path('', views.index, name="ride"),
    path('submit', views.rideInfo, name="rideInfo"),
    path('processsing', views.statusUpdate, name="statusUpdate"),
    path('success', views.rideSuccessful, name="rideSuccessful"),
    path('drive_or_ride/', views.drive_or_ride, name="drive_or_ride"),  # Add this pattern
]

