# Generated by Django 5.0.4 on 2024-05-23 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_products_product_delivery_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_tax_rate',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='product_specification',
            field=models.TextField(blank=True, default=0, null=True),
        ),
    ]