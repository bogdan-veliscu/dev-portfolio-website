from django.db import models
from app_header.models import AppDetails
from django.db.models import OneToOneField
from app_download.models import DownloadSection
from app_features.models import MainFeatures
from app_about.models import AppMission
from testimonials.models import TestimonialsSection
from app_screens.models import AppScreens

from django.utils.translation import gettext as _

# Create your models here.


class AppLanding(models.Model):
    header = OneToOneField(
        AppDetails, verbose_name=_("details"), on_delete=models.CASCADE)
    version = models.CharField(("v0.1.0"), max_length=50)
    logo = models.ImageField(upload_to='img/')
    download_info = models.OneToOneField(
        DownloadSection, verbose_name=_("downloads"), on_delete=models.CASCADE)
    features = models.OneToOneField(
        MainFeatures, verbose_name=_("features"), on_delete=models.CASCADE)
    about_info = models.OneToOneField(
        AppMission, verbose_name=_("mission"), on_delete=models.CASCADE)
    reviews = models.OneToOneField(
        TestimonialsSection, verbose_name=_("reviews"), on_delete=models.CASCADE, null=True, blank=True)
    screens = models.OneToOneField(
        AppScreens, verbose_name=_("screens"), on_delete=models.CASCADE)

    def __str__(self):
        return self.header.title
