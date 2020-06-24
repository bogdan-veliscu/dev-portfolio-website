from django.db import models
from app_header.models import AppDetails
from django.db.models import OneToOneField
from app_download.models import DownloadSection
from django.utils.translation import gettext as _

# Create your models here.


class AppLanding(models.Model):
    header = OneToOneField(
        AppDetails, verbose_name=_("details"), on_delete=models.CASCADE)
    version = models.CharField(("v0.1.0"), max_length=50)
    logo = models.ImageField(upload_to='img/')
    download_info = models.OneToOneField(
        DownloadSection, verbose_name=_("downloads"), on_delete=models.CASCADE)

    def __str__(self):
        return self.header.title