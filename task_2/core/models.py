from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    promo_code = models.CharField(max_length=124, blank=True, null=True)
    bonus = models.IntegerField(default=0, null=True, blank=True)


class InvitationCode(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    invitation_code = models.CharField(max_length=124, blank=True, null=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()