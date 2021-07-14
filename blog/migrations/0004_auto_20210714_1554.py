# Generated by Django 3.2.5 on 2021-07-14 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_profile_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(default=datetime.date.today, verbose_name='birth date'),
        ),
    ]
