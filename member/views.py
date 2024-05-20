from django.shortcuts import render
from .models import Member,Messages
from django.shortcuts import get_object_or_404,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from product.models import Products
from .forms import ProductsForm

def profile(request,username):
    if request.user.is_authenticated:
        if request.user.username == username:
            member = get_object_or_404(Member,username = request.user.username)
            context = {'member': member,'request':request}
            return render(request,'member/user_page.html',context)
        else: 
            messages.add_message(request,messages.ERROR,'Username did not matched!')
            return redirect('home')
    else:
        return redirect('registration:login')
    
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
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductsForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False) 
                product.name = request.user 
                product.sellor_name = request.user.username  
                product.save()  
                return redirect('product:home') 
            else:
                print(form.errors)  
        else:
            form = ProductsForm()
            return render(request, 'member/add_product.html', {'form': form})
    return redirect('registration:login')    

def update_product(request,pk):

    if request.user.is_authenticated:
        product = get_object_or_404(Products,id = pk)
        if request.user == product.sellor_name:
            return redirect('product:home')
        if request.method == 'POST':
            form = ProductsForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product:home')
        else:
            form = ProductsForm(instance=product)
            context = {'form':form}
            return render(request,'member/update_product.html',context)
    return redirect('registration:login')
    
def user_products(request, username):
    if request.user.is_authenticated:
        User = get_user_model()
        user = get_object_or_404(User, username=username)
        products = Products.objects.filter(name=user)
        context = {'request': request, 'products': products}
        return render(request, 'member/my_products.html', context)
    return redirect('registration:login')
def del_prod(request,pk):
    
    if request.user.is_authenticated:
        product = get_object_or_404(Products,id = pk)
        product.delete()
        return redirect('member:user_products',username=request.user)
    
    return redirect('registration:login')

def wishlist(request,pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products,id = pk)
        member = Member.objects.get(username = request.user.username)
        member.user_wish_list.add(product)
        member.save()
        return redirect('product:home')
    return redirect('product:home')

def cart(request,pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products,id=pk)
        member = get_object_or_404(Member,username = request.user.username)
        member.user_cart_list.add(product)
        member.save()
        return redirect('product:home')
    return redirect('registration:login')

def view_wishlist(request):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, username = request.user.username)
        products = member.user_wish_list.all()
        context = {'products':products}
        return render(request,'member/wishlist.html',context)
    return redirect('registration:login')

def remove_wishlist_item(request,pk):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, username = request.user.username)
        product = member.user_wish_list.get(id = pk)
        product.user_wish_list.clear()
        member.save()
        return redirect('member:wishlist_page')
    return redirect('registration:login')

def view_cart(request):

    if request.user.is_authenticated:

        member = get_object_or_404(Member, username = request.user.username)
        products = member.user_cart_list.all()
        context = {'products':products}
        return render(request,'member/cart.html',context)
    return redirect('registration:login')

def remove_cart_item(request,pk):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, username = request.user.username)
        product = member.user_cart_list.get(id = pk)
        product.user_cart_list.clear()
        member.save()
        return redirect('member:cart_page')
    return redirect('registration:login')

