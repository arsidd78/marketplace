from django.db import models
from django.contrib.auth import get_user_model
from product.models import Products

User = get_user_model()

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=13)
    user_profile_picture = models.ImageField(upload_to='users/dp', null=True, blank=True)
    user_wish_list = models.ManyToManyField(Products, blank=True, related_name='wishlisted_users')
    user_cart_list = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='user_cart_list')
    user_recent_purchase = models.ForeignKey(Products, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='user_recent_purchase')
    user_purchases = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    user_recent_sales = models.ForeignKey(Products, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='user_recent_sales')
    user_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    user_search_history = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='user_search_history')
    user_interest = models.ForeignKey(Products, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='user_interest')
    user_followers_no = models.IntegerField()
    user_following_no = models.IntegerField()
    user_notifications_no = models.IntegerField()
    user_followers = models.CharField(max_length=100, null=True, blank=True)
    user_following = models.CharField(max_length=100, null=True, blank=True)
    user_messages_received = models.TextField(verbose_name='Messages Received', null=True, blank=True)
    user_attachedfile_receive = models.FileField(upload_to='users/rec/att', null=True, blank=True)
    user_attachedfile_send = models.FileField(upload_to='users/send/att', null=True, blank=True)
    user_messages_send = models.TextField(verbose_name='Messages Sent', null=True, blank=True)
