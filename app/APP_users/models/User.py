# IMPORTS
import uuid
from django.contrib import admin
from django.db import models

# MODELS
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

## MODEL MANAGER
### Django Model Manager -> A model's manager is an object through which Django models perform database queries. Each Django model has at least one manager, and you can create custom managers in order to customise database access
class UserManager(BaseUserManager):
    def _createUser(self, username, password, is_staff, is_superuser):
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            username=username,

            is_staff=is_staff,
            is_superuser=is_superuser
        )

        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password):
        user = self._createUser(username, password, False, False)
        return user

    def create_superuser(self, username, password):
        superUser = self._createUser(username, password, True, True)
        return superUser

## MODEL
class User(AbstractBaseUser, PermissionsMixin):
    uuid            = models.UUIDField(default=uuid.uuid4, editable=False)
    username        = models.CharField(max_length=140, null=False, blank=False, unique=True)
    password        = models.CharField(max_length=140, null=False, blank=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD  = 'username'
    objects         = UserManager()

    def __str__(self):
        return self.username

## ADMIN
class AdminUser(admin.ModelAdmin):
    list_display = (
        # 'uuid'
        'id', 'username', 'password',
        'is_staff', 'is_superuser'
    )