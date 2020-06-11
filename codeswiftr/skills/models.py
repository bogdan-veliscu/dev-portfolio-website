from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()


class Skill(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    name = models.TextField()
    linkedin_verified = models.BooleanField(default=False)
    upsight_score = models.IntegerField(default=0)
    linkedin_endorsments = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=100)

    def __str__(self):
        return self.name
