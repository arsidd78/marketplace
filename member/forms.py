from django import forms
from product.models import Products
from member.models import Member


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'product_name', 'product_price','product_description', 'product_specification','product_images', 
            'product_images2', 'product_images3', 'product_images4', 'product_images5',
            'product_category', 'product_quantity', 'company_name', 'product_website'
        ]
        widgets = {
            'product_images': forms.ClearableFileInput(attrs={'id': 'id_product_images'}),
            'product_images2': forms.ClearableFileInput(attrs={'id': 'id_product_images2'}),
            'product_images3': forms.ClearableFileInput(attrs={'id': 'id_product_images3'}),
            'product_images4': forms.ClearableFileInput(attrs={'id': 'id_product_images4'}),
            'product_images5': forms.ClearableFileInput(attrs={'id': 'id_product_images5'}),
        }
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user_profile_picture', 'user_phone_number', 'user_website', 'user_about']
        widgets = {
            'user_profile_picture': forms.ClearableFileInput(attrs={'class': 'user_profile_pic', 'id': 'profile_picture', 'accept': 'image/*', 'onchange': 'previewImage(event)'}),
            'user_phone_number': forms.TextInput(attrs={'class': 'phone_no', 'placeholder': 'add phone_no', 'max_length': 13}),
            'user_website': forms.URLInput(attrs={'class': 'user_website', 'placeholder': 'enter your website'}),
            'user_about': forms.Textarea(attrs={'class': 'about', 'placeholder': 'describe yourself'})
        }