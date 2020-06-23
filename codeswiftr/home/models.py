from django.db import models
from app_header.models import AppDetails
from django.db.models import OneToOneField

# Create your models here.


class AppLanding(models.Model):
    header = OneToOneField(
        AppDetails, verbose_name=(""), on_delete=models.CASCADE)
    version = models.CharField(("v0.1.0"), max_length=50)
    logo = models.ImageField(upload_to='img/')
