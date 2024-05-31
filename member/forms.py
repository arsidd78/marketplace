from django import forms
from product.models import Products
from member.models import Member


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_description', 'product_price', 'product_discounted_price', 'product_specification', 'product_images', 'product_images2', 'product_images3', 'product_images4', 'product_images5', 'product_category', 'product_quantity', 'company_name', 'product_website']
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user_profile_picture','user_phone_number','user_website','user_about']
        widgets = {
            'user_phone_number':forms.TextInput(attrs={'class':'phone_no','placeholder':'add phone_no','max_length':13}),
            'user_website':forms.URLInput(attrs={'class':'user_website','placeholder':'enter your website'}),
            'user_about': forms.Textarea(attrs={'class':'about','placeholder':'describe yourself'})
        }