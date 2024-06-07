from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('user_profile/<str:username>/', views.profile, name='profile'),
    path('chat-with-sellor/<int:pk>/',views.chat,name="chat"),
    path('chat_system/<int:pk>/',views.chat_system,name='chat_system'),
    path('chat_system_del_chat/<int:pk>/<int:product_id>/',views.del_chats,name='remove_message'),
    path('add_product/',views.add_product,name='add_product_page'),
    path('update_product/<int:pk>/',views.update_product,name='update'),
    path('user_products/<username>/',views.user_products,name='user_products'),
    path('delete_prod/<int:pk>/',views.del_prod,name='delete_product'),
    path('adding_wishlist/<int:pk>/',views.wishlist,name='add_to_wishlist'),
    path('adding_cart/<int:pk>/',views.cart,name='add_to_cart'),
    path('wishlist_view/',views.view_wishlist,name='wishlist_page'),
    path('cart_view/',views.view_cart,name='cart_page'),
    path('remove_item_wishlist/<int:pk>/',views.remove_wishlist_item,name='remove_wish_item'),
    path('remove_item_cart/<int:pk>/',views.remove_cart_item,name='remove_cart_item'),  
    path('order_cart/',views.order_cart,name='order_cart'),
    path('order_confirmation/',views.order_confirmation,name='confirmation'),
    path('purchase_orders/',views.purchase_orders,name='purchase_orders'),
    path('registration/',views.register,name='register'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('recent_sales',views.sold_products,name='sold_products'),
]