from django.db import models
from django.contrib.auth.models import User
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    birthdate = models.DateField(verbose_name="birth date", default= date.today)


    def __str__(self):
        return f'{self.user.username}'