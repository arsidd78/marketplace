from django.shortcuts import render,get_object_or_404,redirect
from .models import Products
from .forms import PurchaseForm
import os
from collections import deque


# Create your views here.

def home(request):
    products = Products.objects.order_by('-product_name')[:5]
    context = {'products':products,'request':request}
    return render(request,'product/index.html',context=context)

def product_details(request,pk):
    product = get_object_or_404(Products,id=pk)
    context = {'product':product}
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
                product.buyer = request.user
                product.price = item.product_price
                product.product = item
                product.save()
                return render(request,'member/invoice.html')
        else:
            item = get_object_or_404(Products,id=pk)
            form = PurchaseForm()
            return render(request,'product/purchase_page.html',{'form':form,'item':item})
    else:
        return redirect('registration:login')
