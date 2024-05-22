# Generated by Django 5.0.4 on 2024-05-22 06:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_products_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateField(auto_now_add=True)),
                ('posted_time', models.DateField(auto_now=True)),
                ('buyer_phone', models.CharField(max_length=13)),
                ('buyer_address', models.CharField(max_length=200)),
                ('buyer_city', models.CharField(max_length=100)),
                ('buyer_state', models.CharField(max_length=100)),
                ('buyer_zip', models.CharField(max_length=10)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.products')),
            ],
        ),
    ]
