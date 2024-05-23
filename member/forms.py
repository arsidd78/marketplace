from django import forms
from product.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_description', 'product_price', 'product_discounted_price', 'product_specification', 'product_images', 'product_images2', 'product_images3', 'product_images4', 'product_images5', 'product_category', 'product_quantity', 'company_name', 'product_website']
