# Generated by Django 4.2.13 on 2024-07-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Credentials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
    ]
