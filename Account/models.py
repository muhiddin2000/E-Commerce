from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+[1-9]\d{1,14}$',
                                 message='Phone number must be entered in the format: "+999999999". Up to 14 digits allowed.')
    username = models.CharField('Phone Number', validators=[phone_regex], max_length=13, unique=True)
    first_name = models.CharField(max_length=70, null=True)
    last_name = models.CharField(max_length=50, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'password']

    def __str__(self):
        return "{} ||| {}".format(self.username, self.first_name)
