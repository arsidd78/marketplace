# Generated by Django 5.0.4 on 2024-05-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_remove_member_user_wish_list_member_user_wish_list'),
        ('product', '0015_alter_products_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user_wish_list',
            field=models.ManyToManyField(blank=True, related_name='wishlisted_users', to='product.products'),
        ),
    ]