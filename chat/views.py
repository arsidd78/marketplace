from django.shortcuts import render, redirect, get_object_or_404
from product.models import Products
from member.models import Messages
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
                sender = sender,
                receiver = product.name,
                message = body
            )
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully'})
        else:
            product = get_object_or_404(Products, id=pk)
            sender = request.user
            messages = Messages.objects.filter(sender = sender , receiver = product.name)
            context = {'product': product, 'messages': messages}
            return render(request, 'chat/chatPage.html', context)
    return redirect('registration:login')
