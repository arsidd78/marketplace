from django.urls import path 
from . import views

app_name = 'registration'
# Urls:
urlpatterns = [
    path('authentication/',views.authentication,name='authenticate'),
    path('login/',views.login_view,name='login'),    
    path('signup/',views.signup_page,name='signup_page'),
    path('register/',views.signup,name='register'),
]