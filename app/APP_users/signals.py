# IMPORTS
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

# DJANGO REST FRAMEWORK
from rest_framework.authtoken.models import Token

# MODELS
from APP_users.models.User import User
from APP_users.models.Profile import Profile

# MAIN
## Create User Token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

## Create Profile
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
