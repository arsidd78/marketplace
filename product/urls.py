from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<int:pk>/',views.product_details,name='details'),
    path('purchase/<int:pk>/',views.purchase_page,name='purchase_page'),
    path('categories/',views.categories_page,name='categories_page'),
    path('prod_by_cat/<str:category>/',views.product_by_category,name='prod_cat'),
]
