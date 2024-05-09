# Generated by Django 5.0.4 on 2024-05-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_products_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_images',
            field=models.ImageField(height_field=300, upload_to='products/', width_field=300),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_images2',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='products/', width_field=300),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_images3',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='products/', width_field=300),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_images4',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='products/', width_field=300),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_images5',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='products/', width_field=300),
        ),
    ]