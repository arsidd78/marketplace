from django.urls import path 
from . import views
# Urls:
urlpatterns = [
    path('authentication/',views.authentication,name='authenticate'),
    path('login/',views.login,name='login'),    
]