from django.shortcuts import render,get_object_or_404
from .models import Products,SocialHandlers

# Create your views here.

def home(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request,'product/index.html',context=context)

def product_details(request,pk):
    product = get_object_or_404(Products,id=pk)
    context = {'product':product}
    return render(request,'product/details.html',context)
