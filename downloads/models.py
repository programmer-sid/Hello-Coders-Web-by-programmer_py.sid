from django.db import models


class Download(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=2847)
    description = models.CharField(max_length=500)
