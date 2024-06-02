from django.db import models
from django.contrib.auth import get_user_model
from product.models import Products,Purchase


User = get_user_model()

class Messages(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='product')
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField(max_length=500)
    conversation_time = models.DateField(auto_now_add= True)
    attachment = models.FileField(upload_to=f'users/chats/attachments', null=True,blank=True)
    def __str__(self):
        return self.message

class Member(models.Model):
    # User Personal Info:
    username = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=320)
    user_website = models.URLField(null=True,blank=True)
    user_phone_number = models.CharField(max_length=13)
    user_about = models.TextField(max_length=500,null=True,blank=True)
    user_profile_picture = models.ImageField(upload_to='users/dp', null=True, blank=True , default='users/default/defaultdp.png')
    # User Activities:
    user_wish_list = models.ManyToManyField(Products,blank=True, related_name='user_wish_list')
    user_cart_list = models.ManyToManyField(Products, blank=True, related_name='user_cart_list')
    user_recent_purchase = models.ManyToManyField(Products,related_name='user_recent_purchase')
    user_purchases = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    user_recent_sales = models.ManyToManyField(Products, related_name='user_recent_sales')
    user_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,default= 0)
    user_search_history = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='user_search_history')
    user_interest = models.ManyToManyField(Products, auto_created=True)
    user_followers_no = models.IntegerField(default=0)
    user_following_no = models.IntegerField(default=0)
    user_followers = models.CharField(max_length=100, null=True, blank=True)
    user_following = models.CharField(max_length=100, null=True, blank=True)
    # User Chats:
    user_messages_received = models.ManyToManyField(Messages)
    user_attachedfile_receive = models.FileField(upload_to='users/rec/att', null=True, blank=True)
    user_attachedfile_send = models.FileField(upload_to='users/send/att', null=True, blank=True)
    user_messages_send = models.TextField(verbose_name='Messages Sent', null=True, blank=True)
    def __str__(self):
        return self.username
    
class SalesOrder(models.Model):
    sellor = models.ForeignKey(User,on_delete=models.CASCADE)
    sale_order = models.ManyToManyField(Purchase)
    def __str__(self) -> str:
        return self.sellor.username


