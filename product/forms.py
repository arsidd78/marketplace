from django.forms import ModelForm
from member.models import Invoice

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        exclude = 'user'
        fields = "__all__"