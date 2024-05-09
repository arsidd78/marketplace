from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView

app_name = 'registration'
# Urls:
urlpatterns = [
    path('authentication/',views.authentication,name='authenticate'),
    path('login/',views.login_view,name='login'),    
    path('signup/',views.signup_page,name='signup_page'),
    path('register/',views.signup,name='register'),
    path('signout/',views.log_out,name='signout'),
]