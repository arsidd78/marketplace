# Generated by Django 5.0.4 on 2024-05-15 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user_profile_picture',
            field=models.ImageField(blank=True, default='users/default/defaultdp.png', null=True, upload_to='users/dp'),
        ),
    ]
