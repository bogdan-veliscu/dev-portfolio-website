from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects',
                             on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    company = models.TextField()
    client = models.TextField()

    started_at = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(default=3)

    def __str__(self):
        return self.name
