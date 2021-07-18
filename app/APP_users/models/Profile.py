# IMPORTS
import uuid
from django.contrib import admin
from django.db import models

# MODELS
from APP_users.models.User import User   # using extended User Model

## MODEL MANAGER

## MODEL
class Profile(models.Model):
    # Required
    user                = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    uuid                = models.UUIDField(default=uuid.uuid4, editable=False)

    # Not Required
    firstName           = models.CharField(max_length=140, null=True, blank=True)
    lastName            = models.CharField(max_length=140, null=True, blank=True)
    email               = models.CharField(max_length=140, null=True, blank=True)

    def __str__(self):
        return self.user.username

## ADMIN
class AdminProfile(admin.ModelAdmin):
    list_display = (
        # 'uuid'
        'id', 'user',
        'firstName', 'lastName', 'email'
    )