from django.shortcuts import render,get_object_or_404,redirect
from .models import Products,SocialHandlers
import os


# Create your views here.

def home(request):
    products = Products.objects.all()
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