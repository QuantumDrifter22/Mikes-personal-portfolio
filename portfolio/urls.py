from django.urls import path, include
from . import views



urlpatterns = [
    path('about/', views.aboutme, name='aboutme'),
    path('', views.home_view, name='home'),
]
