from django.shortcuts import render, redirect, get_object_or_404
from product.models import Products
from member.models import Messages,Member
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.db.models import Max
from marketplace.custom_decorators import profile_required

@csrf_exempt
@profile_required
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
@profile_required
def SellorChatPage(request):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, user=request.user)
        latest_messages = Messages.objects.filter(receiver= request.user).values('sender').annotate(latest_conversation_time=Max('conversation_time'))
        messages = []
        for latest in latest_messages:
            latest_msg = Messages.objects.filter(sender=latest['sender'], conversation_time=latest['latest_conversation_time']).first()
            if latest_msg:
                messages.append(latest_msg)
        
        # Sort messages by latest conversation time in descending order
        messages = sorted(messages, key=lambda x: x.conversation_time, reverse=True)
        
        context = {'messages': messages,'member':member}
        return render(request, 'chat/sellorChat.html', context)
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
            for chat in received_messages:
                chat.read = True
                chat.save()
            sent_messages = member.user_messages_send.filter(receiver=msg.sender).all().order_by('-conversation_time')
            messages = list(received_messages) + list(sent_messages)
            messages.sort(key=lambda x: x.conversation_time)
            context = {'msg': msg,'received_messages':received_messages,'sent_messages':sent_messages,'messages':messages}
            return render(request, 'chat/receiverChat.html', context)
    return redirect('registration:login')