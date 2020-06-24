from django.db import models

# Create your models here.


class AppMission(models.Model):
    title = models.CharField(("title"), max_length=100)
    subtitle = models.CharField(("subtitle"), max_length=100)
    description = models.CharField(("description"), max_length=200)
    image = models.ImageField(upload_to='img/')
    top_features = models.ManyToManyField(
        "app_features.AppFeature", verbose_name=("features"))

    def __str__(self):
        return self.title
