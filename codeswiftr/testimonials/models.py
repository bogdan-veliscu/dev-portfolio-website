from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Testimonial(models.Model):
    name = models.CharField(_("name"), max_length=50)
    title = models.CharField(_("title"), max_length=50)
    content = models.CharField(_("content"), max_length=200)
    avatar = models.ImageField(upload_to='img/')
    rating = models.IntegerField(_("rating"), validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])

    def __str__(self):
        return self.name + " " + self.title


class TestimonialsSection(models.Model):
    title = models.CharField(_("title"), max_length=50)
    subtitle = models.CharField(_("subtitle"), max_length=50)
    testimonials = models.ManyToManyField(
        Testimonial, verbose_name=_("testimonials"))

    def __str__(self):
        return self.title
