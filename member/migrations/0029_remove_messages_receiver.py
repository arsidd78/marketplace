# Generated by Django 5.0.4 on 2024-06-02 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0028_remove_messages_user_messages_receiver_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='receiver',
        ),
    ]