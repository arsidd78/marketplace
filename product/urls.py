from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<int:pk>/',views.product_details,name='details')
]
