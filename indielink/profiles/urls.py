# urls.py
from django.urls import path
from .views import profile_view

urlpatterns = [
    # Other URL patterns...
    path('profile/', profile_view, name='profile'),
]
