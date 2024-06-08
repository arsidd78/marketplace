from django.shortcuts import render
from .models import Member,Messages,SalesOrder
from django.shortcuts import get_object_or_404,redirect,HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product.models import Products,Purchase
from .forms import ProductsForm,MemberForm
from django.db.models import Max

def profile(request,username):
    if request.user.is_authenticated:
        if request.user.username == username:
            member = get_object_or_404(Member,username = request.user.username)
            new_sales_no = 0
            try:
                sales = Purchase.objects.filter(sellor = request.user)
                for sale in sales:
                    if sale.read == False:
                        new_sales_no +=1
            except:
                new_sales_no = 0            
            context = {'member': member,'request':request,'new_sales_no':new_sales_no}
            return render(request,'member/user_page.html',context)
        else: 
            messages.add_message(request,messages.ERROR,'Complete Your Profile First')
            return redirect('home')
    else:
        return redirect('registration:login')
    
def chat(request,pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, id = pk)
        receiver = product.name
        all_chats = Messages.objects.filter(sender = request.user,receiver = receiver)
        context ={
            'request':request,
            'all_chats':all_chats,
            'product':product
        }
        return render(request,'member/chat_page.html',context)
    else:
        return redirect('registration:login')
    
def chat_system(request,pk):
    if request.method == 'POST':
        product = get_object_or_404(Products, id = pk)
        receiver = product.name
        sender = request.user
        body = request.POST.get('message')

        if sender.is_authenticated:
            all_chats = Messages.objects.filter(sender = sender,receiver=receiver)
            message = Messages.objects.create(sender=sender,receiver=receiver,message=body)
            message.save()
            return redirect('member:chat', pk = pk)
        else :
            return redirect('registration:login')    
    else:
        return HttpResponse('Error ocur while sending message reload and try again ')
    
def del_chats(request,pk,product_id):
    
    if request.user.is_authenticated:
        message = get_object_or_404(Messages, id = pk)
        receiver = message.receiver
        
        message.delete()
        return redirect('member:chat',pk = product_id) # Redirecting to chat page with the reference of product.
    
    else:
        return redirect('registration:login')

# CRUD operations: s

def add_product(request):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, user = request.user)
        if request.method == 'POST':
            form = ProductsForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False) 
                product.name = request.user 
                product.sellor_name = request.user.username  
                product.save()  
                return redirect('member:user_products',username = request.user) 
            else:
                print(form.errors)  
        else:
            form = ProductsForm()
            return render(request, 'member/add_product.html', {'form': form,'member':member})
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
                return redirect('member:user_products', username = request.user)
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

def order_cart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            member = get_object_or_404(Member, user=request.user)
            cart_products = member.user_cart_list.all()
            purchases = []
            total = []
            
            for product in cart_products:
                sellor = get_object_or_404(Member,user = product.name)
                quantity = request.POST.get(f'product_quantity_{product.id}')
                if quantity:
                    purchase_order = Purchase.objects.create(
                        product=product,
                        buyer=request.user,
                        quantity=int(quantity),
                        sellor=product.name,
                        price=product.product_price,
                        buyer_phone=request.POST.get('phone'),
                        buyer_address=request.POST.get('address'),
                        buyer_city=request.POST.get('city'),
                        buyer_state=request.POST.get('state'),
                        buyer_zip_code=request.POST.get('zip_code')
                    )
                    purchase_order.save()
                    product.product_quantity -= int(quantity)
                    # Total Price:
                    total_price = int(quantity) * product.product_price
                    total.append(total_price)
                    # Buyer Purchase history update:
                    member.user_recent_purchase.add(product)
                    member.user_purchases += product.product_price * int(quantity)
                    # Sellor Sales history update:
                    sellor.user_recent_sales.add(product)
                    sellor.user_sales += product.product_price * int(quantity)
                    product.save()

                    purchase = get_object_or_404(Purchase, id=purchase_order.id)
                    sales = SalesOrder.objects.create(sellor = purchase.sellor)
                    sales.save()
                    sales.sale_order.add(purchase)
                    
                    purchases.append(purchase)
                
            context = {
                'request': request,
                'cart_products': cart_products,
                'purchases': purchases,
                'total':sum(total)
            }
            return render(request, 'member/confirmation.html', context)
        else:
            member = get_object_or_404(Member, user=request.user)
            cart_products = member.user_cart_list.all()
            context = {
                'request': request,
                'cart_products': cart_products,
                'member':member
            }
            return render(request, 'member/cart_order.html', context)
    
    return redirect('registration:login')

def order_confirmation(request):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, user = request.user)
        products = member.user_cart_list.all()
        for product in products:
            product.user_cart_list.clear()
        return render(request,'member/order_confirmation.html')
    return redirect('registration:login')

def purchase_orders(request):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, user=request.user)
        purchases = Purchase.objects.filter(sellor = request.user).order_by('-posted_time')
        totals = []
        for purchase in purchases:
           total =  purchase.price * purchase.quantity
           totals.append(total)   
        context = {'purchases':purchases,'data':zip(purchases,totals),'member':member}
        return render(request, 'member/purchase_orders.html', context)
    return redirect('registration:login')

def dispatch(request,pk):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, user=request.user)
        purchase = get_object_or_404(Purchase, id = pk)
        purchase.delete()
        return redirect('member:purchase_orders')
    return redirect('registration:login')

# Member Create:    
def register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MemberForm(request.POST,request.FILES)
            if form.is_valid():
                member = form.save(commit=False)
                member.user = request.user
                member.username = request.user.username
                member.email = request.user.email
                member.save()
                return redirect('product:home')
        else:
            form = MemberForm()
            context = {'form': form,'request':request}
            return render(request,'member/register.html',context)    
    return redirect('registration:login')  

# Member Update:      
def edit_profile(request):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, user = request.user)
        if request.method == 'POST':
            form = MemberForm(request.POST,request.FILES, instance=member)
            if form.is_valid():
                form.save()
                return redirect('member:profile', username = request.user.username)
            else:
                return HttpResponse('Error in editing Profile')
        else:
            form = MemberForm(instance=member)
            context = {'form':form,'request':request}
            return render(request,'member/edit_profile.html',context)
    return redirect('registration:login')    

def sold_products(request):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, user = request.user)
        sales = SalesOrder.objects.filter(sellor = request.user)
        # quantity = sales.sale_order.product_quantity
        products = member.user_recent_sales.all()
        context = {'products':products}
        return render(request,'member/recent_sales.html',context)
    return redirect('registration:login')



@csrf_exempt
def update_purchase_read_status(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            purchases = Purchase.objects.filter(sellor=request.user, read=False)
            purchases.update(read=True)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'failure'})
    return redirect('registration:login')


