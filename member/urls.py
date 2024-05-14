from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('user_profile/<int:pk>/', views.profile, name='profile'),
]