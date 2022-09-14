from django.db import models
# Create your models here.
class Nasa(models.Model):
    identifier= models.CharField(max_length=80)
    image = models.CharField(max_length=80)
    caption = models.CharField(max_length=80)
    version = models.CharField(max_length=80)
    date = models.DateField(max_length=80)
    

class WhoIs(models.Model):
    ip=models.CharField(max_length=80)
    organization= models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    description= models.CharField(max_length=80)
    creation_date = models.DateField(max_length=80)
