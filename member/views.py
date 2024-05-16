from django.shortcuts import render
from .models import Member,Messages
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
    if request.method == 'POST':
        user = request.user
        body = request.POST.get('message')

        if user.is_authenticated:
            all_chats = Messages.objects.filter(sender = user,receiver=user)
            message = Messages.objects.create(sender=user,receiver=user,message=body)
            message.save()
            context = {'message':message,'all_chats':all_chats}
            return render(request,'member/chat_page.html',context)
        else :
            return redirect('member:login')    
    else:
        return HttpResponse('Error ocur while sending message reload and try again ')