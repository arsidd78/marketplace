# Generated by Django 5.0.4 on 2024-05-08 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.TextField(max_length=500)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price')),
                ('product_specification', models.TextField(blank=True, null=True)),
                ('product_posted_date', models.DateField(auto_now_add=True)),
                ('product_images', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('product_category', models.CharField(max_length=100, verbose_name='category')),
                ('sellor_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialHandlers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_handler1', models.URLField(blank=True, null=True, unique=True)),
                ('social_handler2', models.URLField(blank=True, null=True, unique=True)),
                ('social_handler3', models.URLField(blank=True, null=True, unique=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
    ]
