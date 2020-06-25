from django.db import models


class Blog(models.Model):
    post_num = models.IntegerField()
    date = models.CharField(max_length=12)
    image_url = models.CharField(max_length=2875)
    description = models.CharField(max_length=10000)

