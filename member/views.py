from django.shortcuts import render
from .models import Member
from django.shortcuts import get_object_or_404,redirect,HttpResponse
from django.contrib import messages
# Create your views here.
def profile(request,username):
    if request.user.is_authenticated:
        if request.user.username == username:
            member = get_object_or_404(Member,username = request.user.username)
            context = {'member': member,'request':request}
            return render(request,'member/user_page.html',context)
        else: 
            messages.add_message(request,messages.ERROR,'Username Did not matched!')
            return redirect('home')
    else:
        return redirect('login')
def chat(request):
    if request.user.is_authenticated:
        return render(request,'member/chat_page.html')
    else:
        return redirect('registration:login')
    
def chat_system(request):
    return HttpResponse('Hello World')     
    