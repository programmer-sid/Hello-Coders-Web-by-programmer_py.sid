from django.db import models

class Course(models.Model):
    logo_of_channel = models.CharField(max_length=2875)
    name_of_channel = models.CharField(max_length=15)
    for_which_language = models.CharField(max_length=15)
    link_of_channel = models.CharField(max_length=2857)
    des_of_channel = models.CharField(max_length=250)


