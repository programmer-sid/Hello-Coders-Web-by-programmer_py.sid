from django.db import models
from datetime import date
class YourBlog(models.Model):
    name = models.CharField(max_length=122)
    image_url = models.CharField(max_length=2844)
    des = models.TextField(max_length=5000)
    dt = date.today()
