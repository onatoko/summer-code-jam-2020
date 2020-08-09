# Generated by Django 3.0.8 on 2020-08-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_account_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_active',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', max_length=300, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
