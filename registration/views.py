from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
import logging

logging.basicConfig(filename='registration_logs.log',filemode='a',format='%(asctime)s %(message)s')
# Views:
def authentication(request):
    global user  # This view handles user login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Authenticate user
        if user is not None:
            login(request, user)  # Log in the users
            return redirect('product:home')  
        else:
            messages.error(request, "Invalid username or password")  
            return render(request, 'registration/login.html')  
    else:
        return render(request, 'registration/login.html')  
def log_out(request):
    messages.add_message(request,messages.INFO,'Logged Out!')
    try:
        logout(request)
    except Exception as e:
        logging.error(f'Following exceptions was occur while trying to logout: {e}')   
    finally:     
        return redirect('product:home')    


def login_view(request):  
    return render(request, 'registration/login.html')  


def signup(request): # Registration for the user Logic:
        if request.method == 'POST':
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect('registration:signup_page')
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,last_name=last_name)                               
            user.save()
            return redirect('registration:login')
        else:
            return redirect('product:home')

def signup_page(request):  # Interface for signup
    return render(request, 'registration/signup.html')  # Render the signup template
