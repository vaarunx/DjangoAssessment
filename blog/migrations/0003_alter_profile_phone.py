# Generated by Django 3.2.5 on 2021-07-14 11:27

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
