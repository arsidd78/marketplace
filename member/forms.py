from django.forms import ModelForm
from product.models import Products

# Forms:
class ProductsForm(ModelForm):
    class Meta:
        model = Products
        
        fields = [
        "product_name",
        "product_description",
        "product_price",
        "product_discounted_price",
        "product_specification",
        "product_images",
        "product_images2",
        "product_images3",
        "product_images4",
        "product_images5",
        "product_category",
        "product_quantity",
        "sellor_name",
        "company_name",
        "product_website"
    ]
    def save(self, commit=True, user=None):
        product = super().save(commit=False)
        if user:
            product.name = user  # Assuming 'name' is the field to be set to the username
        if commit:
            product.save()
        return product


    