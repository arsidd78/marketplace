from django.contrib import admin
from .models import Member,Messages,SalesOrder
# Register your models here:
admin.site.register(Member)
admin.site.register(Messages)
admin.site.register(SalesOrder)