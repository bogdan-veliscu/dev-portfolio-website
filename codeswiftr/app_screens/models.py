from django.db import models

# Create your models here.


class Screenshot(models.Model):
    image = models.ImageField(upload_to='img/')


class AppScreens(models.Model):
    title = models.CharField(("title"), max_length=100)
    subtitle = models.CharField(("subtitle"), max_length=100)
    screens = models.ManyToManyField(Screenshot, verbose_name=("screens"))
