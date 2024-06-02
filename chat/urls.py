from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('chat/<int:pk>/',views.chatPage,name='web-chat'),
    path('chat/',views.SellorChatPage,name='sellor-chat'),
]