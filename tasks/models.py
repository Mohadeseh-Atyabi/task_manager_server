from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    title = models.CharField()
    description = models.TextField()
    duration = models.TimeField()
    start_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
