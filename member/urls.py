from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('user_profile/<str:username>/', views.profile, name='profile'),
    path('chat-with-sellor/',views.chat,name="chat"),
    path('chat_system/',views.chat_system,name='chat_system'),
    path('chat_system/del_chat',views.del_chats,name='remove_message'),
    path('add_product/',views.add_product,name='add_product_page'),
    path('update_product/<int:pk>/',views.update_product,name='update'),
    path('user_products/<username>/',views.user_products,name='user_products'),
    path('delete_prod/<int:pk>/',views.del_prod,name='delete_product'),
]