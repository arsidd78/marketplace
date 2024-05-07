from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Views:
def authentication (request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = User(request, username=user_name,password=password ) # authenticating user
        if user is not None:
            login(request,user) # This will log in a user
            return redirect(request,'home') # Redirect to home page
        else:
            msg = messages.add_message(request, messages.ERROR, "Invalid email or password")
            return render(request,'registration/login.html') # If credentials are invalid than it will render login page again with an error message
    else:
        return redirect('home')
    
def login (request):
    return render(request,'registration/login.html')
