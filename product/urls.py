from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<int:pk>/',views.product_details,name='details'),
    path('categories/',views.categories_page,name='categories_page'),
    path('prod_by_cat/<str:category>/',views.product_by_category,name='prod_cat'),
    path('recent_products/',views.recent_products,name='recent_products'),
    path('view_all/',views.view_all,name='view_all'),
    path('payment/<int:pk>/',views.purchase_view,name='purchase_page'),
   
]
