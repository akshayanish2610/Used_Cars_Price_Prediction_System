# urls.py
from django.urls import path
from . import views
app_name = "Used_cars"
urlpatterns = [
    path('', views.predict, name='predict'),
    
    
    # Add other URL patterns as needed
]
