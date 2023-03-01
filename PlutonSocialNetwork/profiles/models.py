from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=14, null=True)
    dateRegister = models.DateTimeField()
    avatar = models.CharField(max_length=250)
    isOnline = models.BooleanField(default=False)
    lastVisit = models.DateTimeField()
    verified = models.BooleanField(default=False)
    birthday = models.DateTimeField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthday} {self.verified}'
