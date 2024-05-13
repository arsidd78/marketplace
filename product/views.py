from django.shortcuts import render,get_object_or_404,redirect
from .models import Products,SocialHandlers
import os
from collections import deque


# Create your views here.

def home(request):
    products = Products.objects.order_by('-product_name')[:5]
    context = {'products':products,'request':request}
    return render(request,'product/index.html',context=context)

def product_details(request,pk):
    product = get_object_or_404(Products,id=pk)
    social_handlers = SocialHandlers.objects.all()
    context = {'product':product}
    return render(request,'product/details.html',context)

def purchase_page(request,pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products,id=pk)
        context = {'product':product}
        return render(request, 'product/purchase_page.html',context)
    else:
        return redirect('registration:login')
def categories_page(request):
    products = Products.objects.all()
    categories = set()
    for product in products:
        categories.add(product.product_category)
    context = {'categories':categories}
    return render(request,'product/categories_page.html',context)
def product_by_category(request,category):
    products = Products.objects.filter(product_category=category)
    context = {'products':products}
    return render(request,'product/pbc.html',context)
def recent_products(request):
    arranged_products = Products.objects.order_by('product_posted_date')
    products = deque(arranged_products)
    context = {'products':products}
    return render(request,'product/recent_prod.html',context)