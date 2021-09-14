from datetime import datetime, date

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    passport_series = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=255, blank=False)


class Cars(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=255, blank=False)
    model = models.CharField(max_length=255, blank=False)


class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Cars, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
