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
            sender = get_object_or_404(Member, user = request.user)
            sender.user_messages_send.add(message)
            
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

def ChatSellor(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            msg = get_object_or_404(Messages, id=pk)
            receiver = get_object_or_404(Member, user = msg.sender)
            sender = get_object_or_404(Member,user = request.user)
            body = request.POST.get('message')
            if body:
                message = Messages.objects.create(
                    sender=request.user,
                    receiver=msg.sender,
                    product=msg.product,
                    message=body
                )
                receiver.user_messages_received.add(message)
                sender.user_messages_send.add(message)

                return JsonResponse({'status': 200, 'message': 'Message sent successfully'})
            else:
                return JsonResponse({'status': 400, 'message': 'Message body is empty'})
        else:
            msg = get_object_or_404(Messages, id=pk)
            member = get_object_or_404(Member, user=request.user)
            received_messages = member.user_messages_received.filter(sender=msg.sender).all().order_by('-conversation_time')
            sent_messages = member.user_messages_send.filter(receiver=msg.sender).all().order_by('-conversation_time')
            messages = list(received_messages) + list(sent_messages)
            messages.sort(key=lambda x: x.conversation_time)
            print(f'**************************{messages}*****************************')
            zip_data = zip(received_messages, sent_messages)
            context = {'msg': msg,'received_messages':received_messages,'sent_messages':sent_messages,'messages':messages}
            return render(request, 'chat/receiverChat.html', context)
    return redirect('registration:login')