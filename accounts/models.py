from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class MysiteUser(AbstractUser):
    nickname = models.CharField(max_length=20, default='')

    class Meta(AbstractUser.Meta):
        pass
