from django.db import models

## MODEL MANAGER

## MODEL
class Media_File(models.Model):
    attachment = models.FileField()

## ADMIN