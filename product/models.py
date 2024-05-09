from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(max_length=500)
    product_price = models.DecimalField('Price',max_digits=7,decimal_places=2)
    product_specification = models.TextField(null= True, blank= True)
    product_posted_date = models.DateField( auto_now_add=True)
    product_images = models.ImageField(upload_to='products/')
    product_images2 = models.ImageField(null=True,blank=True,upload_to='products/')
    product_images3 = models.ImageField(null=True,blank=True,upload_to='products/')
    product_images4 = models.ImageField(null=True,blank=True,upload_to='products/')
    product_images5 = models.ImageField(null=True,blank=True,upload_to='products/')
    product_category = models.CharField('category',max_length=100)
    sellor_name = models.CharField(max_length=100)
    company_name = models.CharField(null= True, blank= True, max_length=200)
    product_website = models.URLField(null= True,blank=True)
    def __str__(self) -> str:
        return self.product_name
    
class SocialHandlers(models.Model):
    product_name = models.ForeignKey(Products,on_delete=models.CASCADE)
    social_handler1 = models.URLField(null=True,blank=True,unique=True)
    social_handler2 = models.URLField(null=True,blank=True,unique=True)
    social_handler3 = models.URLField(null=True,blank=True,unique=True)