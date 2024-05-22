from django.forms import ModelForm
from .models import Purchase

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['buyer_phone','buyer_address','buyer_city','buyer_state','buyer_zip_code','quantity']