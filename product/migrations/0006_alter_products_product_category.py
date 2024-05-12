# Generated by Django 5.0.4 on 2024-05-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_products_product_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_category',
            field=models.CharField(choices=[('ELECTRONICS', 'Electronics'), ('FRUITS', 'fruits')], max_length=100, verbose_name='category'),
        ),
    ]
