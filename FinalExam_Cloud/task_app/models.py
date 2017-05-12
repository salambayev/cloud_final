from django.db import models
from registration.models import User
# Create your models here.


class Task(models.Model):
    content = models.TextField(blank=False, null=False)
    state = models.CharField(blank=False, null=True, max_length=120)
    user = models.ForeignKey(User)