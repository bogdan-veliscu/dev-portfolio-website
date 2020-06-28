from django.db import models

# Create your models here.


class ContactEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

    def __str__(self):
        return '%s -> %s' % (self.name, self.subject)
