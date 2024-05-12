# Generated by Django 5.0.4 on 2024-05-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_products_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_category',
            field=models.CharField(choices=[('ELECTRONICS', 'Electronics'), ('CLOTHING & ACCESSORIES', 'Clothing & Accessories'), ('HOME & KITCHEN', 'Home & Kitchen'), ('BEAUTY & PERSONAL CARE', 'Beauty & Personal Care'), ('HEALTH & FITNESS', 'Health & Fitness'), ('TOYS & GAMES', 'Toys & Games'), ('BOOKS & MEDIA', 'Books & Media'), ('AUTOMOTIVE', 'Automotive'), ('SPORTS & OUTDOORS', 'Sports & Outdoors'), ('PET SUPPLIES', 'Pet Supplies'), ('HOME APPLIANCES', 'Home Appliances'), ('OFFICE SUPPLIES', 'Office Supplies'), ('FURNITURE & DECOR', 'Furniture & Decor'), ('JEWELRY & WATCHES', 'Jewelry & Watches'), ('BABY & TODDLER', 'Baby & Toddler'), ('FOOD & GROCERIES', 'Food & Groceries'), ('ARTS & CRAFTS', 'Arts & Crafts'), ('MUSICAL INSTRUMENTS', 'Musical Instruments'), ('GARDEN & OUTDOOR LIVING', 'Garden & Outdoor Living'), ('TRAVEL & LUGGAGE', 'Travel & Luggage')], max_length=100, verbose_name='category'),
        ),
    ]
