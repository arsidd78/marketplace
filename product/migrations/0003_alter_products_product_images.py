# Generated by Django 5.0.4 on 2024-05-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_products_product_images2_products_product_images3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_images',
            field=models.ImageField(default='nan', upload_to='products/'),
            preserve_default=False,
        ),
    ]
