# IMPORTS
from django.contrib import admin

# MODELS & ADMIN
from .models.User import User, AdminUser
from .models.Profile import Profile, AdminProfile

# REGISTER
admin.site.register(User, AdminUser)
admin.site.register(Profile, AdminProfile)