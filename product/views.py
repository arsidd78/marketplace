from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.core.mail import send_mail
from .models import Products,Purchase,Reviews
from member.models import Member
from .forms import PurchaseForm,ReviewForm
from collections import deque


# Create your views here.

def home(request):
    try: 
        
        member = get_object_or_404(Member, user = request.user)
        products = Products.objects.order_by('-product_posted_date')[:5]
        messages_recieved = member.user_messages_received.all()
        unread_messages = 0
        new_sales_order = 0
        try:
            purchase_orders = Purchase.objects.filter(sellor = request.user)
            for order in purchase_orders:
                if order.read == False:
                  new_sales_order +=1
        except:# Incase there is no sale order
            purchase_orders = None
        for msg in messages_recieved:
            if msg.read == False:
                unread_messages+=1
        
        try: 
            if request.user.is_authenticated:
                items = member.user_interest.all()
                context = {

                    'products':products,
                    'items':items[:5] ,
                    'member':member,
                    'request':request,
                    'unread_messages':unread_messages,
                    'new_sales_order': new_sales_order
                }
        except: # Incase there is no user_interest:
            context = {
                'products':products,
                'request':request,
                'member':member,
                'unread_messages':unread_messages,
                'new_sales_order': new_sales_order
                }
            
        return render(request,'product/index.html',context=context)
    except :    
        products = Products.objects.order_by('-product_posted_date')[:5]
        context = {'products':products}
        return render(request,'product/index.html',context=context)

def product_details(request,pk):
    try:
        member = get_object_or_404(Member, user = request.user)
        product = get_object_or_404(Products,id=pk)
        reviews = Reviews.objects.filter(product=product)
        member.user_interest.add(product)
        
        context = {'product':product,'reviews':reviews,'member':member,'range':[x for x in range(1,6)]}
        return render(request,'product/details.html',context)
    except:
        product = get_object_or_404(Products,id=pk)
        reviews = Reviews.objects.filter(product=product)
        context = {'product':product,'reviews':reviews}
        return render(request,'product/details.html',context)

    
def categories_page(request):
    products = Products.objects.all()
    categories = set()
    images = []

    for product in products:
        categories.add(product.product_category)
    for cat in categories:
        items = Products.objects.filter(product_category=cat)
        item = items[0]
        img = item.product_images
        images.append(img)
    data = zip(images,categories)    

    context = {'data':data}
    return render(request,'product/categories_page.html',context)

def product_by_category(request,category):
    products = Products.objects.filter(product_category=category)
    context = {'products':products}
    return render(request,'product/pbc.html',context)

def recent_products(request):
    products = Products.objects.order_by('-product_posted_date')
    context = {'products':products}
    return render(request,'product/recent_prod.html',context)

def view_all(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request,'product/view_all.html',context)

def purchase_view(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':

            item = get_object_or_404(Products,id=pk)
            form = PurchaseForm(request.POST,request.FILES)
            
            if form.is_valid():
                product = form.save(commit=False)
                product.sellor = item.name
                product.buyer = request.user
                product.price = item.product_price
                product.product = item
                product.save()
                purchase = get_object_or_404(Purchase, id = product.id)
                sellor = get_object_or_404(Member, user = item.name)
                buyer = get_object_or_404(Member, user = request.user)
                # Adjust quantity of products after purchase order
                item.product_quantity -= product.quantity
                sellor.user_recent_sales.add(item)
                sellor.user_sales += product.price * product.quantity
                # Adding records of purchase for buyer:
                buyer.user_recent_purchase.add(item)
                buyer.user_purchases += product.price * product.quantity

                return render(request,'product/confirmation.html',{'item':item,'purchase':purchase})
        else:    
            item = get_object_or_404(Products,id=pk)
            form = PurchaseForm()
            return render(request,'product/purchase_page.html',{'form':form,'item':item})
    else:
        return redirect('registration:login')

def confirmation(request, pk):
    if request.user.is_authenticated:
        purchase = get_object_or_404(Purchase,id = pk)
        product = purchase.product
        member = get_object_or_404(Member, user=request.user)
        selected_quantity = purchase.quantity
        # Recording Purchases:
        member.user_recent_purchase.add(product)
        member.user_purchases += product.product_price
        # Recording sales:
        sellor = get_object_or_404(Member, user = purchase.sellor) # getting sellor profile based on product sellor
        sellor.user_recent_sales.add(product)
        sellor.user_sales += product.product_price
        if product.product_quantity >= selected_quantity:
            product.product_quantity -= selected_quantity
        else:
            return render(request, 'product/error.html', {'message': 'Not enough stock'})
    
        member.user_recent_purchase.add(product)
        total_price = purchase.quantity * purchase.price
        member.user_purchases += total_price
        product.save()
        member.save()
        context = {
            'purchase': purchase,
            'total_price': total_price,
            'request':request
            }
        return render(request, 'product/invoice.html', context)
    return redirect('registration:login')

# Review Create:
def review_create(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, id=pk)
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.reviewer = request.user
                review.save()
                return redirect('product:details', pk=pk)
        else:
            form = ReviewForm()
            return render(request, 'product/review_form.html', {'form': form, 'product': product})
    return redirect('registration:login')

def search(request):
    if request.method == 'POST':
        try :
            member = get_object_or_404(Member, user = request.user)
            search = request.POST.get('search_bar')
            member.user_search_history.add(search) # This will add keywords in search history 
            products = Products.objects.filter(product_name__contains = search)
        except: # Incase anonymous user is searching 
            search = request.POST.get('search_bar') 
            products = Products.objects.filter(product_name__contains = search)

        return render(request, 'product/search_result.html', {'search':search,'products': products})
    else:
        return render(request,'product/search_result.html')

def recommended_products(request):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, user = request.user)
        products = member.user_interest.all()
        return render(request, 'product/recommended.html', {'products':products})
    return redirect('registration:login')