# Generated by Django 5.0.4 on 2024-05-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_products_product_tax_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_specification',
            field=models.TextField(blank=True, null=True),
        ),
    ]
