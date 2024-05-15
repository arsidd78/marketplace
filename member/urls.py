from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('user_profile/<str:username>/', views.profile, name='profile'),
    path('chat-with-sellor/',views.chat,name="chat"),
    path('chat_system/',views.chat_system,name='chat_system'),
]