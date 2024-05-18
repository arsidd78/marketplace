from django.shortcuts import render
from .models import Member,Messages
from django.shortcuts import get_object_or_404,redirect,HttpResponse
from django.contrib import messages
from product.models import Products
from .forms import ProductsForm
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
        all_chats = Messages.objects.filter(sender = request.user,receiver = request.user)
        context ={
            'request':request,
            'all_chats':all_chats
        }
        return render(request,'member/chat_page.html',context)
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
def del_chats(request):

    user = request.user
    if request.user.is_authenticated:
        messages = Messages.objects.filter(sender = user,receiver=user)
        for message in messages:
            message.delete()
            return redirect('member:chat')
    else:
        return redirect('registration:login')

# CRUD operations: 
def add_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)  # Create but don't save the product yet
            product.name = request.user # Set the user as the product creator
            product.sellor_name = request.user.username  # Optionally set the seller's name
            product.save()  # Save the product to the database
            return redirect('product:home')  # Redirect to a success page
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = ProductsForm()
        return render(request, 'member/add_product.html', {'form': form})