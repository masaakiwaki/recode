from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)


class Family(models.Model):
    family_user = models.ForeignKey('User', on_delete=models.CASCADE)
    person = models.CharField(verbose_name='利用者', max_length=255)

    def __str__(self):
            return self.person


class Result(models.Model):
    result_family = models.ForeignKey('Family', on_delete=models.CASCADE)
    temperature = models.FloatField(verbose_name='体温')
    create_at = models.DateTimeField(verbose_name='検温日', auto_now_add=True)

    def __float__(self):
            return self.temperature
