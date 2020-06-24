from django.db import models

# Create your models here.


class AppFeature(models.Model):
    icon = models.CharField(("icon"), max_length=50)
    name = models.CharField(("name"), max_length=100)
    description = models.CharField(("description"), max_length=200)
    position = models.IntegerField()

    def __str__(self):
        return self.name


class MainFeatures(models.Model):

    title = models.CharField(("title"), max_length=100)
    subtitle = models.CharField(("subtitle"), max_length=100)
    image = models.ImageField(upload_to='img/')
    features = models.ManyToManyField(AppFeature, verbose_name=("features"))

    def __str__(self):
        return self.title
