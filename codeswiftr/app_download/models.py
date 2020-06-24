from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class DownloadLink(models.Model):
    url = models.URLField(_("store_url"), max_length=200)
    name = models.CharField(_("name"), max_length=50)
    icon = models.CharField(_("icon"), max_length=50)

    def __str__(self):
        return self.name


class DownloadSection(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.CharField(_("description"), max_length=200)
    links = models.ManyToManyField(DownloadLink, verbose_name=_("links"))

    def __str__(self):
        return self.title
