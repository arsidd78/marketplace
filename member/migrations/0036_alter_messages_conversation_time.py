# Generated by Django 5.0.4 on 2024-06-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0035_remove_member_user_messages_send_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='conversation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]