# Generated by Django 5.0.4 on 2024-06-02 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0030_messages_receiver'),
        ('product', '0025_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.products'),
            preserve_default=False,
        ),
    ]
