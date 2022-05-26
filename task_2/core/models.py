from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    promo_code = models.CharField(max_length=124, blank=True, null=True)
    bonus = models.IntegerField(default=0, null=True, blank=True)


class InvitationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invitation_code = models.CharField(max_length=124, blank=True, null=True)
