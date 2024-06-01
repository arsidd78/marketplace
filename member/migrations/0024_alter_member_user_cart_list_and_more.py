# Generated by Django 5.0.4 on 2024-05-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0023_alter_member_user_email_remove_member_user_interest_and_more'),
        ('product', '0025_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user_cart_list',
            field=models.ManyToManyField(blank=True, related_name='user_cart_list', to='product.products'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_interest',
            field=models.ManyToManyField(auto_created=True, to='product.products'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_recent_purchase',
            field=models.ManyToManyField(related_name='user_recent_purchase', to='product.products'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_recent_sales',
            field=models.ManyToManyField(related_name='user_recent_sales', to='product.products'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_wish_list',
            field=models.ManyToManyField(blank=True, related_name='user_wish_list', to='product.products'),
        ),
    ]