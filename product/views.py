from django.shortcuts import render,get_object_or_404
from .models import Products,SocialHandlers
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request,'product/index.html',context=context)

def product_details(request,pk):
    product = get_object_or_404(Products,id=pk)
    social_handlers = SocialHandlers.objects.all()
    context = {'product':product}
    return render(request,'product/details.html',context)

@login_required(login_url='registration/login/')
def purchase_page(request,pk):
    product = get_object_or_404(Products,id=pk)
    context = {'product':product}
    return render(request, 'product/purchase_page.html',context)