from django.shortcuts import render, redirect, get_object_or_404
from product.models import Products
from member.models import Messages,Member
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q

@csrf_exempt
def chatPage(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, id=pk)
        sender = request.user
        if request.method == 'POST':
            body = request.POST.get('message')
            message = Messages.objects.create(
                product = product,
                sender = sender,
                receiver = product.name,
                message = body
            )
            member = get_object_or_404(Member, user = product.name)
            member.user_messages_received.add(message)
            
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully'})
        else:
            product = get_object_or_404(Products, id=pk)
            sender = request.user
            messages = Messages.objects.filter(Q(sender = request.user)& Q(receiver = product.name),product=product)
            try:
                for msg in messages:
                    buyer = msg.sender # To save the user who initiated chat.
                    break
                context = {'product': product, 'messages': messages,'buyer':buyer}
                return render(request, 'chat/chatPage.html', context)
            except:
                context = {'product': product, 'messages': messages}
                return render(request, 'chat/chatPage.html', context)
    return redirect('registration:login')

def SellorChatPage(request):
    if request.user.is_authenticated:
        messages = Messages.objects.filter(receiver=request.user)
        context = {'messages':messages}
        return render(request,'chat/sellorChat.html',context)
    return redirect('registration:login')
